from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOny(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return bool(obj.owner == request.user or request.user.is_staff)