from django.urls import path
from . import views

app_name='post'

urlpatterns = [
    path('',views.list, name='list'),
    path('write/',views.write, name='write'),
    path('show/<int:post_id>/', views.show, name='show')
]

