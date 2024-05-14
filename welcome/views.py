from django.shortcuts import render
from blog.models import Post

def welcome(request):
    blog_entries = Post.objects.filter(status=1).order_by('-created_on')
    latest_blog_entry = blog_entries.first()
    selected_entries = blog_entries[1:4]
    
    return render(request, 'welcome.html', {'latest_blog_entry': latest_blog_entry, 'selected_entries': selected_entries})

