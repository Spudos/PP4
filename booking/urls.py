from django.urls import path
from . import views
from .views import BookingEditView

urlpatterns = [
    path('', views.booking_page, name='booking'),
    path('booking_form/', views.booking_form, name='booking_form'),
    path('booking/<int:pk>/edit/',
         BookingEditView.as_view(), name='booking_edit'),
    path('booking_success/<int:booking_id>/',
         views.booking_success, name='booking_success'),
]
