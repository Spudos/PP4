from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('user-account/', views.user_account, name='user_account'),
]