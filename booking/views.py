from django.shortcuts import render, redirect
from .models import Sessions
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest

def booking_page(request):
  session_types = Sessions.objects.all()
  
  return render(request, 'booking.html', {'session_types': session_types})

@login_required
def booking_form(request):
    session_type = request.GET.get('session_type')
    if session_type is None:
        return HttpResponseBadRequest("Session type is required")
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            new_booking = form.save(commit=False)
            new_booking.user = request.user
            new_booking.booking_date_time = form.cleaned_data['booking_date_time']
            new_booking.session_type = session_type
            new_booking.save()
            return redirect('booking')
    else:
        initial_data = {'user': request.user.id, 'session_type': session_type}
        form = BookingForm(initial=initial_data)
    return render(request, 'booking_form.html', {'form': form})


