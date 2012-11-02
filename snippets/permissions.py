from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """ Custom permission to only allow owners of an object to edit it."""
    
    def has_permission(self, request, view, obj=None):
        if obj is None:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user
