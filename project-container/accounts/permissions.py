from rest_framework import permissions


class IsAuthenticatedOrWriteOnly(permissions.BasePermission):
    message = 'Only authenticated users have read permissions.'

    def has_permission(self, request, view):
        # allow all POST requests
        if request.method == 'POST':
            return True

        # Otherwise, only allow authenticated requests
        return request.user and request.user.is_authenticated
