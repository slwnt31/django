from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('home/signup/', signup, name='signup'),
    path('home/login', login, name='login'),
    path('home/logout', logout, name='logout')
]
