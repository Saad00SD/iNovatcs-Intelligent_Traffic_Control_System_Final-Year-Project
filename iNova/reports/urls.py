
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.reports,name = 'reports'),
    #Incident Section
    path('incident/' ,views.incident, name = 'incident'),
    path('incident/create/', views.create_incident, name='create_incident'),  # Create a new incident
    path('incident/<int:id>/', views.update_incident, name='update_incident'),  # Update an existing incident
    path('incident/delete/<int:id>/', views.delete_incident, name='delete_incident'),  # Delete an incident


    
    path('traf/',views.traf, name = 'traf'),
    path('traf/add/', views.add_traffic_signal, name='add_traffic_signal'),  # Add this path
    path('traf/update/<int:id>/', views.update_traffic_signal, name='update_traffic_signal'),
    path('traf/delete/<int:id>/', views.delete_traffic_signal, name='delete_traffic_signal'),



    path('monthly/',views.monthly,name = 'monthly'),
    path('weekly/',views.weekly,name = 'weekly'),
    path('annualy/',views.annualy,name = 'annualy'),
 

]
