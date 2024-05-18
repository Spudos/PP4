from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Comment
from booking.models import Sessions, Booking
from datetime import date

def welcome(request):
    blog_entries = Post.objects.filter(status=1).order_by('-created_on')
    latest_blog_entry = blog_entries.first()
    selected_entries = blog_entries[1:4]
    
    session_types = Sessions.objects.all()
    
    unapproved_comments = Comment.objects.filter(approved=0)
    
    return render(request, 'welcome.html', {'latest_blog_entry': latest_blog_entry, 'selected_entries': selected_entries, 'session_types': session_types, 'unapproved_comments': unapproved_comments})

def user_account(request):
    user_bookings = Booking.objects.filter(user=request.user)
    user_past_bookings = user_bookings.filter(appointment__date_time__lt=date.today())
    user_future_bookings = user_bookings.filter(appointment__date_time__gt=date.today())
    

    return render(request, 'user_account.html', {
        'user_bookings': user_bookings,
        'user_past_bookings': user_past_bookings,
        'user_future_bookings': user_future_bookings
    })
    
def delete_booking(request, booking_id):
    if request.method == 'POST':
        booking = get_object_or_404(Booking, id=booking_id)
        booking.delete()
        return redirect('user_account')