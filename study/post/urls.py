from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.list, name='list'),
    path('write/',views.write, name='write'),
    path('show/<int:post_id>/', views.show, name='show')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

