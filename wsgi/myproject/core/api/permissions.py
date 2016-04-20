from rest_framework.permissions import BasePermission

SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS', 'POST']

class IsCompanyOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        Returns true if the user is the owner of the entity
        """
        if request.method in SAFE_METHODS:
            return True
        elif request.method == 'PUT' or request.method == 'PATCH':
            if obj.user == request.user:
                return True
            return False
