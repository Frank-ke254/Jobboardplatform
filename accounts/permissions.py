from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """
    Allows access only to admin users.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'


class IsUser(BasePermission):
    """
    Allows access only to normal users.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'user'
