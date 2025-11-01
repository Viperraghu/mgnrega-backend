from django.db import models

class DistrictPerformance(models.Model):
    district = models.CharField(max_length=100)
    report_year = models.CharField(max_length=20, null=True, blank=True)
    report_month = models.CharField(max_length=20, null=True, blank=True)
    person_days = models.CharField(max_length=50, null=True, blank=True)
    expenditure = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = "mgnrega_district_performance"

    def __str__(self):
        return f"{self.district} - {self.report_month}/{self.report_year}"
