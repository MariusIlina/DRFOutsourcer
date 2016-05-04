from drf_cached_instances.cache import BaseCache
from core.models import Project, TimeUnit, Company
from django.core import serializers

class ProjectCache(BaseCache):

    """Cache for Project model view-set."""

    def project_default_serializer(self, obj):
        """Convert a Project to a cached instance representation."""
        if not obj:
            return None
        #self.project_default_add_related_pks(obj)
        return dict((
            ('id', obj.id),
            ('project_name', obj.project_name),
            self.field_to_json('DateTime', 'pub_date', obj.pub_date),
            ('by_company', obj.by_company.id),
            ('approximate_duration', obj.approximate_duration),
            ('approximate_duration_time_unit', obj.approximate_duration_time_unit.id),
            ('description', obj.description),
            ('work_description', obj.work_description),
            ('slug_name', obj.slug_name),
            ('required_techs', obj.required_techs),
            ('approximate_hours_per_week', obj.approximate_hours_per_week),
            ('payment_type', obj.payment_type.id),
            ('payment_amount', obj.payment_amount),
            ('currency', obj.currency.id),
            ('min_ppl_required', obj.min_ppl_required),
            ('category', obj.category.id)
        ))

    def project_default_loader(self, pk):
        """Load a Project from the database."""
        try:
            obj = Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return None
        else:
            self.project_default_add_related_pks(obj)
            return obj

    def project_default_add_related_pks(self, obj):
        """Add related primary keys to a Project instance."""
        #if not hasattr(obj, '_company_pks'):
            #obj._company_pks = list(obj.by_company.values_list('id', flat=True))
        return []

    def project_default_invalidator(self, obj):
        """Invalidate cached items when the User changes."""
        return []
