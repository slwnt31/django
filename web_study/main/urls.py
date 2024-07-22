from django.urls import path
from . import views
from main.views import index, blog, posting

app_name = 'main'

urlpatterns = [
    #path('', views.index, name="index"),
    path('blog/', views.blog, name="blog"),
    path('blog/<int:pk>', views.posting, name="posting"),
    path('blog/new_post/', views.new_post, name="new_post")
    ]
