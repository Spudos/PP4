from django.test import TestCase
from django.urls import reverse
from blog.models import Post, Comment
from booking.models import Sessions
from django.utils import timezone

class WelcomeViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        post1 = Post.objects.create(title='First Post', status=1, created_on=timezone.now())
        post2 = Post.objects.create(title='Second Post', status=1, created_on=timezone.now())
        post3 = Post.objects.create(title='Third Post', status=1, created_on=timezone.now())
        session1 = Sessions.objects.create(name='Session 1')
        session2 = Sessions.objects.create(name='Session 2')
        comment1 = Comment.objects.create(text='Unapproved Comment 1', approved=0)
        comment2 = Comment.objects.create(text='Unapproved Comment 2', approved=0)

    def test_welcome_view(self):
        response = self.client.get(reverse('welcome'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'welcome.html')
        self.assertEqual(response.context['latest_blog_entry'].title, 'First Post')
        self.assertQuerysetEqual(
            response.context['selected_entries'],
            ['<Post: Second Post>', '<Post: Third Post>']
        )
        self.assertQuerysetEqual(
            response.context['session_types'],
            Sessions.objects.all()
        )
        self.assertQuerysetEqual(
            response.context['unapproved_comments'],
            Comment.objects.filter(approved=0)
        )
