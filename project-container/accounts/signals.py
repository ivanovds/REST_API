import logging
from django.utils import timezone
from django.core.signals import request_started
from django.dispatch import receiver
from django.contrib.auth import user_logged_in, user_login_failed
from rest_framework_jwt.serializers import jwt_decode_handler
from django.contrib.auth.models import User

from .models import UserLoginActivityLog, UserRequestActivityLog
from project.settings import JWT_AUTH

JWT_AUTH_HEADER_PREFIX = JWT_AUTH['JWT_AUTH_HEADER_PREFIX']


@receiver(request_started)
def log_last_request_datetime(sender, environ, **kwargs):
    if 'HTTP_AUTHORIZATION' in environ:
        if JWT_AUTH_HEADER_PREFIX in environ['HTTP_AUTHORIZATION']:
            token = environ['HTTP_AUTHORIZATION'].split(' ')[-1]
            try:
                payload = jwt_decode_handler(token)
                last_request_datetime, created = UserRequestActivityLog.objects.update_or_create(
                    user=User.objects.get(username=payload['username']),
                    defaults={
                        'request_method': environ.get('REQUEST_METHOD', '<unknown>')[:255],
                        'path_info': environ.get('PATH_INFO', '<unknown>')[:255],
                    }
                )
            except Exception as e:
                logging.error("log_last_request_datetime: %s" % e)


@receiver(user_logged_in)
def log_user_logged_in_success(sender, user, request, **kwargs):
    print(type(request.META))
    try:
        user_agent_info = request.META.get('HTTP_USER_AGENT', '<unknown>')[:255],
        user_login_activity_log, created = UserLoginActivityLog.objects.update_or_create(
            login_username=user.username,
            status=UserLoginActivityLog.SUCCESS,
            defaults={'login_IP': get_client_ip(request),
                      'user': user,
                      'login_username': user.username,
                      'user_agent_info': user_agent_info,
                      'login_datetime': timezone.now(),
                      },
        )
        last_request_datetime, created = UserRequestActivityLog.objects.update_or_create(
            user=user,
            defaults={
                'request_method': request.META.get('REQUEST_METHOD', '<unknown>')[:255],
                'path_info': request.META.get('PATH_INFO', '<unknown>')[:255],
            }
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
                      'login_datetime': timezone.now(),
                      },
        )
    except Exception as e:
        logging.error("log_user_logged_in request: %s, error: %s" % (request, e))


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
