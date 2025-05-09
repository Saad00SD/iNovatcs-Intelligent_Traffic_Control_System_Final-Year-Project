from django import forms
from .models import IncidentReport
from .models import TrafficSignal


class IncidentReportForm(forms.ModelForm):
    class Meta:
        model = IncidentReport
        fields = ['incident_id', 'date', 'location', 'description', 'status']

    def clean_incident_id(self):
        # Get the incident_id entered by the user
        incident_id = self.cleaned_data.get('incident_id')

        # Check if the incident_id already exists in the database
        if IncidentReport.objects.filter(incident_id=incident_id).exists():
            raise forms.ValidationError("This Incident ID already exists. Please enter a unique ID.")

        return incident_id

class TrafficSignalForm(forms.ModelForm):
    class Meta:
        model = TrafficSignal
        fields = ['location', 'signal_state', 'signal_timer', 
                  'lane_1_vehicle_count', 'lane_2_vehicle_count', 
                  'lane_3_vehicle_count', 'lane_4_vehicle_count', 
                ]

