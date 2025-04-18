from django.urls import path
from users import views as user_views  # Import views from the users app
from anomaly import views as anomaly_views  # Import views from the anomaly app
from traffic import views as traffic_views  # Import views from the traffic app
from reports import views as reports_views  # Import views from the reports app

urlpatterns = [
    # User-related URLs
    path('register/', user_views.register, name='register'),
    path('login/', user_views.user_login, name='login'),
    path('logout/', user_views.user_logout, name='logout'),

    # Protected Pages (only accessible by logged-in users)
    path('home/', user_views.user_home, name='home'),  # Redirect to home or dashboard after login
    path('anomaly/', anomaly_views.anomaly, name='anomaly'),  # Protected anomaly page
    path('traffic/', traffic_views.traffic, name='traffic'),  # Protected traffic page
    path('reports/', reports_views.reports, name='reports'),  # Protected reports page
]