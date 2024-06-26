from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "draft"), (1, "Public"))
CATEGORY = ((0, "Fitness"),
            (1, "Lifestyle"),
            (2, "Cardio"),
            (3, "Nutrition"),
            (4, "Motivation"),
            (5, "Shopping"),
            (6, "Weight"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="blog_posts")
    last_update = models.DateTimeField(auto_now=True)
    content = models.TextField()
    image = CloudinaryField('image', default='none')
    excerpt = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    category = models.IntegerField(choices=CATEGORY, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)


class Meta:
    ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)


class Meta:
    ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
