from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to only allow admins to edit objects, others can read only.
    """

    def has_permission(self, request, view):
        # Allow GET (read-only) requests for all users
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        # Allow non-read-only requests only for admins
        return request.user and request.user.is_staff
