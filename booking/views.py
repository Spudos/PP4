from django.shortcuts import render, redirect
from .models import Sessions, Appointments
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from datetime import datetime

import pdb

def booking_page(request):
  session_types = Sessions.objects.all()
  
  return render(request, 'booking.html', {'session_types': session_types})

@login_required
def booking_form(request):
    session_type = request.GET.get('session_type')
    if session_type is None:
        return HttpResponseBadRequest("Session type is required")
    user_name = request.user.get_full_name()
    
    available_appointments = Appointments.objects.filter(available=True).order_by("date_time")
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        pdb.set_trace()
        if form.is_valid():
            new_booking = form.save(commit=False)
            new_booking.user = request.user

            date_time_str = form.cleaned_data['booking_date_time']
            input_format = "%B %d, %Y, %I %p"
            parsed_date_time = datetime.strptime(date_time_str, input_format)
            output_format = "%Y-%m-%d %H:%M:%S"
            formatted_date_time = parsed_date_time.strftime(output_format)
            
            new_booking.booking_date_time = formatted_date_time
            new_booking.session_type = session_type
            new_booking.save()
            return redirect('booking')
    else:
        initial_data = {'user': request.user.id, 'session_type': session_type}
        form = BookingForm(initial=initial_data)
        
    return render(request, 'booking_form.html', {'form': form, 'user_name': user_name, 'available_appointments': available_appointments})


