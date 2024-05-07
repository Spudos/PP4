from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogEntries.as_view(), name='blog'),
]