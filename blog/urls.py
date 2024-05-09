from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogEntries.as_view(), name='blog'),
    path('<slug:slug>/', views.BlogDetail.as_view(), name='blog_detail'),
]