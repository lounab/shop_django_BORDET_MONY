from django.urls import path
from . import views

app_name ='appdjango1'
urlpatterns = [    
    path('list',views.list_view, name='list_view'),
    path('login',views.login, name='login'),
    path('chat/<str:room_name>/', views.room, name='room'),
    path('chat', views.chat, name='chat'),
    path('<id>', views.detail_view),
    path('<id>/update', views.update_view),
    path('<id>/delete', views.delete_view),
]