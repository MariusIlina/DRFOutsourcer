from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User
from core.models import Company, Project

SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']
OWNER_METHODS = ['PUT', 'PATCH', 'DELETE']

class IsCompanyOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        Returns true if the user is the owner of the entity or is staff
        """
        if request.method in SAFE_METHODS or request.method == 'POST':
            return True
        elif request.method in OWNER_METHODS:
            if obj.user == request.user or obj.user.is_staff:
                return True
            return False


class IsProjectOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        Returns true:
         - on PUT/PATCH if the authenticated user is the user who created the
        company that posted the project
         - on POST if the authenticated user is the user who created the company
         that is trying to create the project
        """
        if request.method in SAFE_METHODS:
            return True
        # Allow users to edit only projects that belong to their companies
        elif request.method in OWNER_METHODS:
            if obj.by_company.user == request.user:
                return True
            return False
        # Allow users to post new projects only on behalf of their own companies
        elif request.method == 'POST':
            companies = Company.objects.filter(user=request.user, id=request.data['by_company'])
            raise Exception({"message": request.user.id, "animal": request.data['by_company']})
            if len(companies) is not 0:
                return True
            return False


class BidderIsCompanyOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        Returns true if the user who wants to bid on a project is the owner
        of the company on which behalf he does the bidding
        """
        return True
