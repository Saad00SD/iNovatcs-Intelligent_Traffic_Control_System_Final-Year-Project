from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('traffic/', views.traffic, name='traffic'),    
    path('footage_1/', views.footage_1, name='footage_1'),
    path('footage_2/', views.footage_2, name='footage_2'),
    path('footage_3/', views.footage_3, name='footage_3'),
    path('footage_4/', views.footage_4, name='footage_4'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
