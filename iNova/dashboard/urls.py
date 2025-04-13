
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard,name = 'dashboard'),

# In this urls I have to add Traffic, Anomaly and Reports
    # path('anomaly/', views.anomaly,name = 'anomaly'),
    # path('traffic/', views.traffic,name = 'traffic'),
    # path('reports/', views.reports,name = 'reports'),

]
