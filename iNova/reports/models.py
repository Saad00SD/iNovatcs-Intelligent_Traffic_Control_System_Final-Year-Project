from django.db import models


class IncidentReport(models.Model):
    incident_id = models.CharField(max_length=50, unique=True)
    date = models.DateField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=50)

    class Meta:
        db_table = 'reports_incidentreport'  # Same table name used

    def __str__(self):
        return f"Incident Report: {self.incident_id} at {self.location}"
