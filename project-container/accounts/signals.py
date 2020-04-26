from django.contrib.auth.models import User
import logging
from django.core.signals import request_started
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import authenticate, user_logged_in, user_login_failed

from .models import UserLoginActivityLog


@receiver(request_started)
def save_last_request_datetime(sender, environ, **kwargs):
    print(sender)


@receiver(user_logged_in)
def log_user_logged_in_success(sender, user, request, **kwargs):
    try:
        user_agent_info = request.META.get('HTTP_USER_AGENT', '<unknown>')[:255],
        user_login_activity_log, created = UserLoginActivityLog.objects.update_or_create(
            login_username=user.username,
            status=UserLoginActivityLog.SUCCESS,
            defaults={'login_IP': get_client_ip(request),
                      'user': user,
                      'login_username': user.username,
                      'user_agent_info': user_agent_info,
                      },
        )
    except Exception as e:
        logging.error("log_user_logged_in request: %s, error: %s" % (request, e))


@receiver(user_login_failed)
def log_user_logged_in_failed(sender, credentials, request, **kwargs):
    try:
        user_agent_info = request.META.get('HTTP_USER_AGENT', '<unknown>')[:255],
        user_login_activity_log, created = UserLoginActivityLog.objects.update_or_create(
            login_username=credentials['username'],
            status=UserLoginActivityLog.FAILED,
            defaults={'login_IP': get_client_ip(request),
                      'user_agent_info': user_agent_info,
                      },
        )
    except Exception as e:
        # log the error
        logging.error("log_user_logged_in request: %s, error: %s" % (request, e))


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
