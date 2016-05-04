from drf_cached_instances.cache import BaseCache
from core.models import Project, TimeUnit, Company, Currency, Category, PaymentTypes
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
            self.field_to_json('by_company', 'by_company', model=Company, pks=obj._company_pks),
            ('approximate_duration', obj.approximate_duration),
            self.field_to_json(
                'approximate_duration_time_unit',
                'approximate_duration_time_unit',
                model=TimeUnit,
                pks=obj._time_unit_pks
            ),
            ('description', obj.description),
            ('work_description', obj.work_description),
            ('slug_name', obj.slug_name),
            ('required_techs', obj.required_techs),
            ('approximate_hours_per_week', obj.approximate_hours_per_week),
            self.field_to_json('payment_type', 'payment_type', model=PaymentTypes, pks=obj._payment_type_pks),
            ('payment_amount', obj.payment_amount),
            self.field_to_json('currency', 'currency', model=Currency, pks=obj._currency_pks),
            ('min_ppl_required', obj.min_ppl_required),
            self.field_to_json('category', 'category', model=Category, pks=obj._category_pks)
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
        if not hasattr(obj, '_company_pks'):
            obj._company_pks = list(obj.by_company.values_list('id', flat=True))
        if not hasattr(obj, '_time_unit_pks'):
            obj._time_unit_pks = list(obj.approximate_duration_time_unit.values_list('id', flat=True))
        if not hasattr(obj, '_payment_type_pks'):
            obj._payment_type_pks = list(obj.payment_type.values_list('id', flat=True))
        if not hasattr(obj, '_currency_pks'):
            obj._currency_pks = list(obj.currency.values_list('id', flat=True))
        if not hasattr(obj, '_category_pks'):
            obj._category_pks = list(obj.category.values_list('id', flat=True))

    def project_default_invalidator(self, obj):
        """Invalidate cached items when the Project changes."""
        return []
