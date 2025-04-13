
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
    path('monthly/',views.monthly,name = 'monthly'),
    path('weekly/',views.weekly,name = 'weekly'),
    path('annualy/',views.annualy,name = 'annualy'),
 

]
