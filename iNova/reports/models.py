from django.db import models


class IncidentReport(models.Model):
    incident_id = models.CharField(max_length=50,unique=True)
    date = models.DateField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.incident_id

