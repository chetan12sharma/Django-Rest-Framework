from rest_framework import permissions


class IsCurrentUserOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # this method is safe
            return True
        else:
            # this method is not safe
            # only owners are granted permissions for unsafe methods
            return obj.owner == request.user
