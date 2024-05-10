from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post
from .forms import CommentForm

class BlogEntries(generic.ListView):
  model = Post
  queryset = Post.objects.filter(status=1).order_by('-created_on')
  template_name = "blog.html"
  paginate_by = 6

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