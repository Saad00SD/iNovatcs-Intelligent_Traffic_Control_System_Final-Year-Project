from django.urls import path
from . import views
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views



urlpatterns = [
    path('', views.anomaly, name='anomaly'),
    path('footage_1/', views.foot_1, name='foot_1'),
    path('footage_2/', views.foot_2, name='foot_2'),
    path('footage_3/', views.foot_3, name='foot_3'),
    path('footage_4/', views.foot_4, name='foot_4'),
    
    # Update for accident detection on footage_2
    path('video_feed_uploaded/footage_2/', views.video_feed_uploaded, {'footage_type': 'accident'}, name='video_feed_footage_2'),
    
    path('video_feed_uploaded/footage_1/', views.video_feed_uploaded, {'footage_type': 'fire'}, name='video_feed_footage_1'),
    path('video_feed_uploaded/footage_3/', views.video_feed_uploaded, {'footage_type': 'fire'}, name='video_feed_footage_3'),
    path('video_feed_uploaded/footage_4/', views.video_feed_uploaded, {'footage_type': 'fire'}, name='video_feed_footage_4'),

    path("detection/", views.alert_update, name="detection"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
