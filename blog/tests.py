from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post, Comment
from blog.views import BlogDetail


class BlogDetailTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        test_user = User.objects.create_user(
            username='testuser', password='12345')
        test_user.save()
        test_post = Post.objects.create(title='Test Post',
                                        slug='test-post',
                                        status=1,
                                        author=test_user)
        test_post.save()
        test_comment = Comment.objects.create(post=test_post,
                                              name='Test User',
                                              email='test@example.com',
                                              body='Test comment text',
                                              approved=True)
        test_comment.save()

    def test_blog_detail_get_method(self):
        # Test the get method of BlogDetail view
        response = self.client.get(reverse('blog_detail',
                                           kwargs={'slug': 'test-post'}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_detail.html')

    def test_blog_detail_post_method(self):
        # Test the post method of BlogDetail view
        self.client.force_login(User.objects.get(username='testuser'))
        comment_data = {
            'email': 'test@example.com',
            'name': 'Test User',
            'body': 'Test comment text',
        }
        response = self.client.post(reverse('blog_detail',
                                            kwargs={'slug': 'test-post'}),
                                    data=comment_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Post.objects.get(
            slug='test-post').comments.count(), 2)

    def test_blog_like_post_method(self):
        # Test the post method of BlogLike view
        self.client.force_login(User.objects.get(username='testuser'))
        response = self.client.post(reverse('blog_like',
                                    kwargs={'slug': 'test-post'}))
        self.assertEqual(response.status_code, 302)
        