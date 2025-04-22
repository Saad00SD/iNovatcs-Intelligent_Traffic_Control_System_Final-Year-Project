from django.db import models


class IncidentReport(models.Model):
    incident_id = models.CharField(max_length=50, unique=True)
    date = models.DateField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Incident Report: {self.incident_id} at {self.location}"
    

class TrafficSignal(models.Model):
    location = models.CharField(max_length=255,unique=True)  # Location of the intersection
    signal_state = models.CharField(max_length=50, choices=[('Red', 'Red'), ('Yellow', 'Yellow'), ('Green', 'Green')])
    signal_timer = models.IntegerField()  # Timer for how long the signal stays on
    lane_1_vehicle_count = models.IntegerField(default=0)
    lane_2_vehicle_count = models.IntegerField(default=0)
    lane_3_vehicle_count = models.IntegerField(default=0)
    lane_4_vehicle_count = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically set when the entry is created

    def __str__(self):
        return f"Traffic Signal at {self.location}"

