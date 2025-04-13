
from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.anomaly,name = 'anomaly'),
    path('fire-detection/' ,views.fire_detection, name = 'fire_detection'),
    path('fire-detection/upload', views.upload_fire_video, name = 'upload_fire_video'),

]
