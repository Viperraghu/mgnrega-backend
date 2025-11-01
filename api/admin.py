
from django.contrib import admin
from .models import DistrictPerformance

@admin.register(DistrictPerformance)
class DistrictPerformanceAdmin(admin.ModelAdmin):
    list_display = ('district', 'report_year', 'report_month', 'person_days', 'expenditure')
    list_filter = ('report_year', 'district')
    search_fields = ('district',)
