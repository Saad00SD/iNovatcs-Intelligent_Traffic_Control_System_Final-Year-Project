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

from django.shortcuts import render
from django.db.models import Count
from datetime import timedelta
from django.utils import timezone
from .models import IncidentReport


def weekly(request):
    today = timezone.now().date()

    report_type = request.GET.get('report_type', 'weekly')  # Default to 'weekly' if no selection is made

    # Weekly Report
    start_of_week = today - timedelta(days=today.weekday())  # Monday of the current week
    end_of_week = start_of_week + timedelta(days=6)  # Sunday of the current week

    start_date = request.GET.get('start_date', start_of_week)
    end_date = request.GET.get('end_date', end_of_week)

    if isinstance(start_date, str):
        start_date = timezone.datetime.strptime(start_date, '%Y-%m-%d').date()
    if isinstance(end_date, str):
        end_date = timezone.datetime.strptime(end_date, '%Y-%m-%d').date()

    weekly_incidents = IncidentReport.objects.filter(date__range=[start_date, end_date])
    total_weekly_incidents = weekly_incidents.count()
    open_weekly_incidents = weekly_incidents.filter(Q(status__iexact='Open') | Q(status__iexact='OPEN') | Q(status__iexact='open')).count()
    closed_weekly_incidents = weekly_incidents.filter(Q(status__iexact='Closed') | Q(status__iexact='CLOSED')).count()

    # Monthly Report
    month = request.GET.get('month', today.month)
    year = request.GET.get('year', today.year)
    
    monthly_incidents = IncidentReport.objects.filter(date__year=year, date__month=month)
    total_monthly_incidents = monthly_incidents.count()
    open_monthly_incidents = monthly_incidents.filter(Q(status__iexact='Open') | Q(status__iexact='OPEN') |Q(status__iexact='open')).count()
    closed_monthly_incidents = monthly_incidents.filter(Q(status__iexact='Closed') | Q(status__iexact='CLOSED') | Q(status__iexact='closed')).count()

    return render(request, 'weeklyRepo/weekly.html', {
        'weekly_incidents': weekly_incidents,
        'total_weekly_incidents': total_weekly_incidents,
        'open_weekly_incidents': open_weekly_incidents,
        'closed_weekly_incidents': closed_weekly_incidents,
        'start_date': start_date,
        'end_date': end_date,
        'month': month,
        'year': year,
        'monthly_incidents': monthly_incidents,
        'total_monthly_incidents': total_monthly_incidents,
        'open_monthly_incidents': open_monthly_incidents,
        'closed_monthly_incidents': closed_monthly_incidents,
        'report_type': report_type,  # Pass the selected report type to the template
        'weekly_chart_data': [total_weekly_incidents, open_weekly_incidents, closed_weekly_incidents],
        'monthly_chart_data': [total_monthly_incidents, open_monthly_incidents, closed_monthly_incidents],
    })


def monthly(request):
    return render(request, 'PeriodRepo/monthly.html')

# def weekly(request):
#     return render(request, 'weeklyRepo/weekly.html')

def annualy(request):
    return render(request, 'PeriodRepo/annualy.html')
