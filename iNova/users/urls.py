from django.urls import path
from .views import register,user_home,user_login,user_logout
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('',user_home,name = 'home'),
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout',user_logout,name = 'logout')
]