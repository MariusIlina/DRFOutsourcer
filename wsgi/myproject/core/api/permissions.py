from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User
from core.models import Company, Project, Bid
from types import MethodType

SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS', 'POST']
OWNER_METHODS = ['PUT', 'PATCH', 'DELETE']

class PermissionToolSet:
    """
    Provides a set of tools for static operations on permissions
    """
    def __init__(self):
        return self

    @staticmethod
    def check_http_and_ownership(http_method, current_user, object_user):
        """
        Checks if the http method is in SAFE_METHODS and if the user is object owner
        """
        if http_method in SAFE_METHODS:
            return True
        elif http_method in OWNER_METHODS:
            if current_user == object_user:
                return True
            return False

    @staticmethod
    def user_owns_creator_company(http_method, http_keyword, http_object, current_user):
        """
        Checks if the user who is trying to bid, comment or post a project is actually
        owner of the company on which behalf he's trying to do such actions
        """
        if http_method == 'POST' and http_keyword in http_object:
            companies = Company.objects.filter(user=current_user, id=http_object[http_keyword])
            if len(companies) > 0:
                return True
            return False
        return True


class IsCompanyOwner(BasePermission):
    """
    Manages permissions for the Company model
    """
    def has_object_permission(self, request, view, obj):
        """
        Returns true if the user is the owner of the company which
        is being modified/deleted
        """
        return PermissionToolSet.check_http_and_ownership(request.method, request.user, obj.user)


class IsEntityOwner(BasePermission):
    """
    Manages permissions for Entities
    Entities are models that are related to the Company model
    """
    def has_object_permission(self, request, view, obj):
        """
        Returns true if the authenticated user is the user who created the
        company that created the entity which is being modified/deleted
        """
        raise Exception(obj.user)
        return PermissionToolSet.check_http_and_ownership(request.method, request.user, obj.by_company.user)

    def has_permission(self, request, view):
        """
        Returns true if the authenticated user is the user who created the
        company that is creating this new entity
        """
        return PermissionToolSet.user_owns_creator_company(request.method, 'by_company', request.data, request.user)


class EditorIsStaff(BasePermission):
    """
    Certain API methods restrict some http_methods
    """
    def has_object_permission(self, request, view, obj):
        """
        Allow reading from anyone but deny posting, editing or deleting
        """
        if request.method in OWNER_METHODS:
            if request.user.is_staff:
                return True
            return False
        return True

    def has_permission(self, request, view):
        """
        Allow creation only for staff
        """
        if request.user.is_staff:
            return True
        return False
