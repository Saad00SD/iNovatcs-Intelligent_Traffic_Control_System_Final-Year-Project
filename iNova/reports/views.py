from django.shortcuts import render,redirect
from .models import IncidentReport  # Assuming you have an IncidentReport model
from .forms import IncidentReportForm
from django.http import JsonResponse
from django.db.models import Q  # Correct import for Q


def create_incident(request):
    if request.method == 'POST':
        form = IncidentReportForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new incident report to the database
            return redirect('incident')  # Redirect to the incident list page
        else:
            # If the form is not valid (due to the duplicate incident_id), the error will be displayed
            return render(request, 'incidentRepo/create_incident.html', {'form': form})
    else:
        form = IncidentReportForm()

    return render(request, 'incidentRepo/create_incident.html', {'form': form})

def update_incident(request, id):
    incident = IncidentReport.objects.get(id=id)
    if request.method == 'POST':
        form = IncidentReportForm(request.POST, instance=incident)
        if form.is_valid():
            form.save()
            return redirect('incident')  # Redirect to the incident list page
    else:
        form = IncidentReportForm(instance=incident)
    
    return render(request, 'incidentRepo/update_incident.html', {'form': form})

def delete_incident(request, id):
    incident = IncidentReport.objects.get(id=id)
    if request.method == 'POST':
        incident.delete()
        return redirect('incident')  # Redirect to the incident list page
    
    return render(request, 'incidentRepo/delete_incident.html', {'incident': incident})

def reports(request):
    return render(request, 'websites/reports.html')

# def incident(request):
#     return render(request, 'incidentRepo/incident.html')


def incident(request):
    search_query = request.GET.get('search', '')  # Get search query from the URL

    # Filter incidents by Incident ID or Location if there's a search query
    incident_reports = IncidentReport.objects.all()

    if search_query:
        incident_reports = incident_reports.filter(
            Q(incident_id__icontains=search_query) |  # Search by Incident ID
            Q(location__icontains=search_query)       # Search by Location
        )

    return render(request, 'incidentRepo/incident.html', {'incident_reports': incident_reports, 'search_query': search_query})


def traf(request):
    return render(request, 'trafficRepo/traf.html')

def monthly(request):
    return render(request, 'PeriodRepo/monthly.html')

def weekly(request):
    return render(request, 'weeklyRepo/weekly.html')

def annualy(request):
    return render(request, 'PeriodRepo/annualy.html')
