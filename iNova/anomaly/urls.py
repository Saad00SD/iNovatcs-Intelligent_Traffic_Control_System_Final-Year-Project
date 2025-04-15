
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('', views.anomaly,name = 'anomaly'),
    # path('fire-detection/' ,views.fire_detection, name = 'fire_detection'),
    # path('fire-detection/upload', views.upload_fire_video, name = 'upload_fire_video'),

    path('footage_1/', views.foot_1, name='foot_1'),
    path('footage_2/', views.foot_2, name='foot_2'),
    path('footage_3/', views.foot_3, name='foot_3'),
    path('footage_4/', views.foot_4, name='foot_4'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
