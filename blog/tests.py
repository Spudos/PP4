from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from blog.models import Post
from blog.views import BlogEntries
from django.contrib.auth.models import User

class BlogEntriesTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='your_username', email='your_email@example.com', password='your_password', first_name='First', last_name='Last', date_joined=timezone.now())
        Post.objects.create(title='Test Post 1', status=1, author=user, slug='1', created_on=timezone.now())
        Post.objects.create(title='Test Post 2', status=1, author=user, slug='2', created_on=timezone.now())

    def test_blog_entries_view(self):
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('post_list' in response.context)
        
        posts = response.context['post_list']
        self.assertEqual(len(posts), 2)
        self.assertTemplateUsed(response, 'blog.html')

class BlogDetailTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='your_username', email='your_email@example.com', password='your_password', first_name='First', last_name='Last', date_joined=timezone.now())
        cls.user = User.objects.create_user(username='testuser', password='12345')
        cls.post = Post.objects.create(title='Test Post', author=user, status=1, slug='test-post')

    def test_blog_detail_view(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('blog_detail', kwargs={'slug': self.post.slug}))
        self.assertEqual(response.status_code, 200)

        self.assertTrue('blog' in response.context)
        self.assertEqual(response.context['blog'], self.post)


        self.assertTemplateUsed(response, 'blog_detail.html')
    
    def test_blog_detail_post_method(self):
        self.client.force_login(self.user)

        comment_data = {
            'email': 'test@example.com',
            'name': 'Test User',
            'text': 'Test comment text',
        }

        response = self.client.post(reverse('blog_detail', kwargs={'slug': self.post.slug}), data=comment_data)
        self.assertEqual(response.status_code, 200)

        self.assertEqual(self.post.comments.count(), 1)

        self.assertTemplateUsed(response, 'blog_detail.html')