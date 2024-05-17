from django.shortcuts import render
from blog.models import Post, Comment
from booking.models import Sessions

def welcome(request):
    blog_entries = Post.objects.filter(status=1).order_by('-created_on')
    latest_blog_entry = blog_entries.first()
    selected_entries = blog_entries[1:4]
    
    session_types = Sessions.objects.all()
    sessions_a = session_types[0:3]
    sessions_b = session_types[3:6]
    
    unapproved_comments = Comment.objects.filter(approved=0)
    
    return render(request, 'welcome.html', {'latest_blog_entry': latest_blog_entry, 'selected_entries': selected_entries, 'sessions_a': sessions_a, 'sessions_b': sessions_b, 'unapproved_comments': unapproved_comments})

def user_account(request):
    return render(request, 'user_account.html')