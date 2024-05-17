from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm


class BlogEntries(generic.ListView):
  model = Post
  queryset = Post.objects.filter(status=1).order_by('-created_on')
  template_name = "blog.html"
  paginate_by = 4
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    category_mapping = {
        0: 'Fitness',
        1: 'Lifestyle',
        2: 'Cardio',
        3: 'Nutrition',
        4: 'Motivation',
        5: 'Shopping',
        6: 'Weight',
    }
    posts = context['post_list']
    for post in posts:
        post.category_string = category_mapping.get(post.category, 'Other')
    return context

class BlogDetail(View):
  def get(self, request, slug, *args, **kwargs):
    queryset = Post.objects.filter(status=1)
    blog = get_object_or_404(queryset, slug=slug)
    comments = blog.comments.filter(approved=True).order_by("-created_on")
    liked = False
    if blog.likes.filter(id=self.request.user.id).exists():
        liked = True

    return render(
        request,
        "blog_detail.html",
        {
            "blog": blog,
            "comments": comments,
            "commented": False,
            "liked": liked,
            "comment_form": CommentForm()
        },
  )
    
  def post(self, request, slug, *args, **kwargs):
    queryset = Post.objects.filter(status=1)
    blog = get_object_or_404(queryset, slug=slug)
    comments = blog.comments.filter(approved=True).order_by("-created_on")
    liked = False
    if blog.likes.filter(id=self.request.user.id).exists():
        liked = True

    comment_form = CommentForm(data=request.POST)
    
    if comment_form.is_valid():
      comment_form.instance.email = request.user.email
      comment_form.instance.name = request.user.username
      comment = comment_form.save(commit=False)
      comment.post = blog
      comment.save()
    else:
      comment_form = CommentForm()
    
    return render(
        request,
        "blog_detail.html",
        {
            "blog": blog,
            "comments": comments,
            "commented": True,
            "liked": liked,
            "comment_form": CommentForm()
        },
  )
    
class BlogLike(View):
  def post(self, request, slug, *args, **kwargs):
    blog = get_object_or_404(Post, slug=slug)
    if blog.likes.filter(id=request.user.id).exists():
        blog.likes.remove(request.user)
    else:
        blog.likes.add(request.user)

    return HttpResponseRedirect(reverse('blog', args=[slug]))