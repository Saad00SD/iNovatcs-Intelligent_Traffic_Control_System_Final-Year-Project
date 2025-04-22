from django.shortcuts import render,redirect
from .models import IncidentReport  
from .forms import IncidentReportForm
from django.http import JsonResponse
from django.db.models import Q  
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect




def create_incident(request):
    if request.method == 'POST':
        form = IncidentReportForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('incident') 
        else:
            return render(request, 'incidentRepo/create_incident.html', {'form': form})
    else:
        form = IncidentReportForm()

    return render(request, 'incidentRepo/create_incident.html', {'form': form})


def update_incident(request, id):
    incident = IncidentReport.objects.get(id=id)
    
    if request.method == 'POST':
        # Exclude the incident_id field during update
        form = IncidentReportForm(request.POST, instance=incident)
        if form.is_valid():
            # Save the form while ensuring the incident_id stays the same
            form.save()
            return redirect('incident')  # Redirect back to the incident list
    else:
        form = IncidentReportForm(instance=incident)

    return render(request, 'incidentRepo/update_incident.html', {'form': form, 'incident': incident})



def delete_incident(request, id):
    incident = IncidentReport.objects.get(id=id)
    if request.method == 'POST':
        incident.delete()
        return redirect('incident')  
    
    return render(request, 'incidentRepo/delete_incident.html', {'incident': incident})

@login_required
def reports(request):
    return render(request, 'websites/reports.html')

# def incident(request):
#     return render(request, 'incidentRepo/incident.html')

from django.core.paginator import Paginator


@login_required
def incident(request):
    search_query = request.GET.get('search', '')  # Get search query from the URL

    # Filter incidents by Incident ID or Location if there's a search query
    incident_reports = IncidentReport.objects.all()

    if search_query:
        incident_reports = incident_reports.filter(
            Q(incident_id__icontains=search_query) |  # Search by Incident ID
            Q(location__icontains=search_query) |
        Q(description__icontains=search_query)  # Search by Description      # Search by Location
        )

    # Order the queryset by a field, e.g., `incident_id` or `date`
    incident_reports = incident_reports.order_by('incident_id')  # You can change 'incident_id' to another field like 'date'

    # Pagination: Show 10 records per page
    paginator = Paginator(incident_reports, 10)
    page_number = request.GET.get('page')  # Get the page number from the URL
    page_obj = paginator.get_page(page_number)

    return render(request, 'incidentRepo/incident.html', {
        'incident_reports': page_obj.object_list, 
        'search_query': search_query,
        'page_obj': page_obj
    })


from .models import TrafficSignal
@login_required
def traf(request):
    search_query = request.GET.get('search', '')  # Get search query from the URL

    traffic_signals = TrafficSignal.objects.all().order_by('location')  # Or 'timestamp' or another field

    if search_query:
        traffic_signals = traffic_signals.filter(
            Q(location__icontains=search_query) |  # Search by location
            Q(signal_state__icontains=search_query)  # Search by signal state
        )

    # Pagination: Show 6 records per page
    paginator = Paginator(traffic_signals, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'trafficRepo/traf.html', {'traffic_signals': page_obj, 'search_query': search_query})

#     return render(request, 'trafficRepo/traf.html')

from .forms import TrafficSignalForm 

@login_required
def add_traffic_signal(request):
    if request.method == 'POST':
        form = TrafficSignalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('traf') 
    else:
        form = TrafficSignalForm()

    return render(request, 'trafficRepo/add_traffic_signal.html', {'form': form})

@login_required
def update_traffic_signal(request, id):
    traffic_signal = TrafficSignal.objects.get(id=id)
    
    if request.method == 'POST':
        form = TrafficSignalForm(request.POST, instance=traffic_signal)
        if form.is_valid():
            form.save()
            return redirect('traf')
    else:
        form = TrafficSignalForm(instance=traffic_signal)

    return render(request, 'trafficRepo/update_traffic_signal.html', {'form': form})

from django.shortcuts import get_object_or_404, render, redirect
from .models import TrafficSignal

@login_required
def delete_traffic_signal(request, id):
    # Get the traffic signal object or return a 404 if not found
    traffic_signal = get_object_or_404(TrafficSignal, id=id)

    # If the request is a POST (user confirmed deletion)
    if request.method == 'POST':
        traffic_signal.delete()  # Delete the traffic signal
        return redirect('traf')  # Redirect back to the traffic reports page

    # If it's a GET request, render the confirmation page
    return render(request, 'trafficRepo/confirm_delete.html', {'traffic_signal': traffic_signal})

    

def monthly(request):
    return render(request, 'PeriodRepo/monthly.html')

def weekly(request):
    return render(request, 'weeklyRepo/weekly.html')

def annualy(request):
    return render(request, 'PeriodRepo/annualy.html')
