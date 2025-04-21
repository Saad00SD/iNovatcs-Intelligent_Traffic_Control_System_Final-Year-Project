from django import forms
from reports.models import IncidentReport
from .models import TrafficData

class VideoUploadForm(forms.Form):
    video_file = forms.FileField()

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
    
from django import forms
from .models import TrafficData

class LocationForm(forms.ModelForm):
    class Meta:
        model = TrafficData
        fields = ['location', 'police_contact', 'hospital_contact', 'fire_contact']
        widgets = {
            'location': forms.TextInput(attrs={'class': 'bg-gray-800 text-white p-2 rounded'}),
            'police_contact': forms.TextInput(attrs={'class': 'bg-gray-800 text-white p-2 rounded'}),
            'hospital_contact': forms.TextInput(attrs={'class': 'bg-gray-800 text-white p-2 rounded'}),
            'fire_contact': forms.TextInput(attrs={'class': 'bg-gray-800 text-white p-2 rounded'}),
        }
