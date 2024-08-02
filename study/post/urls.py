from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name='post'

urlpatterns = [
    path('',views.list, name='list'),
    path('write/',views.write, name='write'),
    path('show/<int:post_id>/', views.show, name='show'),
    path('updateget/<str:post_id>/', views.updateget, name='updateget'),
    path('deleteget/<int:post_id>/', views.deleteget, name='deleteget'),
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    path('<int:post_pk>/likes/', views.likes, name='likes'),
    path('search/', views.search, name='search'),
]

urlpatterns += static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)