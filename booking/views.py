from django.shortcuts import render, redirect, get_object_or_404
from .models import Sessions, Appointments, Booking
from .forms import BookingForm, BookingEditForm
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.urls import reverse
from datetime import date
from django.db.models import Q
from django.conf import settings
from django.core.mail import send_mail


def booking_page(request):
  session_types = Sessions.objects.all()
  
  return render(request, 'booking.html', {'session_types': session_types})


@login_required
def booking_form(request):
    session_type = request.GET.get('session_type')
    if session_type is None:
        return HttpResponseBadRequest("Session type is required")
    user_name = request.user.get_full_name()
    
    current_date = date.today()
    available_appointments = Appointments.objects.filter(Q(booking__isnull=True) & Q(date_time__gt=current_date)).order_by("date_time")
    
    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            new_booking = form.save(commit=False)
            new_booking.user = request.user
            new_booking.session_type = session_type
            appointment_id = request.POST.get('appointment')
            appointment_instance = get_object_or_404(Appointments, id=appointment_id)
            new_booking.appointment = appointment_instance
            new_booking.save()
            return redirect(reverse('booking_success', kwargs={'booking_id': new_booking.id}))
        else:
            return HttpResponseBadRequest("Form data is not valid")
    else:
        initial_data = {'user': request.user.id, 'session_type': session_type}
        form = BookingForm(initial=initial_data)
    
    if available_appointments:
        return render(request, 'booking_form.html', {'form': form, 'user_name': user_name, 'available_appointments': available_appointments})
    else:
        return render(request, 'booking_full.html') 


def booking_success(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    current_user = request.user
    message = booking

    full_message = f"""
        Hey {current_user.first_name}
       
        Thank you for your booking!
        
        Session Type:  {message.session_type}
        
        Notes:  {message.notes}
        
        Date and Time:  {message.appointment.date_time}
        
        I look forward to seeing you.
        
        Many Thanks
        
        Sarah
        Pride Fitness Ltd
        """
    send_mail(
        subject="Received booking submission",
        message=full_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.NOTIFY_EMAIL, current_user.email],
    )

    return render(request, 'booking_success.html', {'booking': booking})

    
class BookingEditView(UpdateView):
    model = Booking
    form_class = BookingEditForm
    template_name = 'booking_edit.html'
    success_url = '/user-account/'

    def form_valid(self, form):
        current_user = self.request.user
        message = form.cleaned_data

        full_message = f"""
            Hey {current_user.first_name}
        
            You have edited your booking!
            
            The revised details are as follows:
            
            Session Type:  {message['session_type']}
            
            Notes:  {message['notes']}
            
            Date and Time:  {message['appointment'].date_time}
            
            I look forward to seeing you.
            
            Many Thanks
            
            Sarah
            Pride Fitness Ltd
            """

        send_mail(
            subject="Received booking submission",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL, current_user.email],
        )
        
        return super().form_valid(form)