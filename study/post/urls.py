from django.urls import path
from . import views

app_name='post'

urlpatterns = [
    path('',views.list, name='list'),
    path('write/',views.write, name='write'),
    path('show/<int:post_id>/', views.show, name='show'),
    # post_id 를 show 함수에서 pk로 정의했는데, pk는 데이터베이스에
    # 저장되어 있는 절대 변하지 않는 맨 앞의 키를 의미한다. 
    # 따라서 show/2를 호출한다면, pk가 2인 글을 호출한다는 의미다.
    
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
]

