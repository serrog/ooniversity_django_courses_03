from django.core.urlresolvers import resolve, reverse
from django.test import TestCase
from django.test import Client
from datetime import date
from django.contrib.auth.models import User
from courses.models import Course
from coaches.models import Coach
from pybursa.views import index
from courses.views import CourseDetailView

def create_courses():
    user1 = User.objects.create(
        username = 'user1'
    )
    user2 = User.objects.create(
        username = 'user2'
    )
    coach1 = Coach.objects.create(
        user=user1, 
        date_of_birth=date.today(),
        gender='M',
        phone='123456',
        address='test address 1',
        skype='test skype 1',
        description='description 1'
    )
    coach2 = Coach.objects.create(
        user=user2, 
        date_of_birth=date.today(),
        gender='F',
        phone='1234567',
        address='test address 2',
        skype='test skype 2',
        description='description 2'
    )
    course1 = Course.objects.create(
        name='course1', 
        short_description='short description 1',
        description='description 1',
        coach=coach1,
        assistant=coach2
    )
    course2 = Course.objects.create(
        name='course2', 
        short_description='short description 2',
        description='description 2',
        coach=coach1,
        assistant=coach2
    )
    


class CoursesListTest(TestCase):

    def test_root_url_resolves_to_index_page(self):
        self.assertEqual(resolve('/').func, index)

    def test_index_view_render_wright_template(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_rendered_correct_html(self):
        client = Client()
        response = client.get('/')
        self.assertContains(response, '<h2>Ooniversity</h2>')
        self.assertContains(response, '<h3>Join our courses!</h3>')

    def test_index_response_contains_correct_context(self):
        client = Client()
        create_courses()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['all_courses']), 2)
        for i, course in enumerate(response.context['all_courses']):
            self.assertEqual(course.name, 'course{}'.format(i+1))
            self.assertEqual(course.short_description, 'short description {}'.format(i+1))
            self.assertEqual(course.description, 'description {}'.format(i+1))

    def test_index_template_contains_correct_links_to_edit_course(self):
        client = Client()
        create_courses()
        response = client.get('/')
        for i in range(1, 3):
            self.assertContains(response, 'href="/courses/edit/{}/"'.format(i))

    def test_index_template_contains_correct_links_to_delete_course(self):
        client = Client()
        create_courses()
        response = client.get('/')
        for i in range(1, 3):
            self.assertContains(response, 'href="/courses/remove/{}/"'.format(i))

    def test_index_template_contains_correct_links_to_add_course(self):
        client = Client()
        response = client.get('/')
        self.assertContains(response, 'href="/courses/add/"')



class CoursesDetailTest(TestCase):

    def test_detail_url_resolves_to_detail_page(self):
        create_courses()
        for i in range(1, 3):
            self.assertEqual(
                resolve('/courses/{}/'.format(i)).func.__name__, 
                CourseDetailView.as_view().__name__
            )

    def test_detail_view_not_render_wright_template_with_non_existing_course(self):
        client = Client()
        response = client.get(reverse('courses:detail', args=(1, )))
        self.assertEqual(response.status_code, 404)

    def test_index_view_render_wright_template(self):
        create_courses()
        client = Client()
        for i in range(1, 3):
            response = client.get(reverse('courses:detail', args=(i,)))
            self.assertEqual(response.status_code, 200)

    def test_rendered_correct_html(self):
        client = Client()
        create_courses()
        response = client.get(reverse('courses:detail', args=(1,)))
        self.assertTemplateUsed(response, 'courses/detail.html')
        self.assertContains(response, '<h3>Coaches</h3>')

    def test_course_detail_response_contains_correct_context(self):
        client = Client()
        create_courses()
        for i in range(1, 3):
            response = client.get(reverse('courses:detail', args=(i,)))
            course = response.context['course_detail']
            self.assertEqual(course.name, 'course{}'.format(i))
            self.assertEqual(course.short_description, 'short description {}'.format(i))
            self.assertEqual(course.description, 'description {}'.format(i))

    def test_course_detail_template_contains_link_to_add_lesson(self):
        client = Client()
        create_courses()
        for i in range(1, 3):
            response = client.get(reverse('courses:detail', args=(i,)))
            self.assertContains(response, 'href="/courses/{}/add_lesson"'.format(i))

    def test_course_detail_template_contains_link_to_coach(self):
        client = Client()
        create_courses()
        for i in range(1, 3):
            response = client.get(reverse('courses:detail', args=(i,)))
            self.assertContains(response, 'href="/coaches/1/"')

    def test_course_detail_template_contains_link_to_assistant(self):
        client = Client()
        create_courses()
        for i in range(1, 3):
            response = client.get(reverse('courses:detail', args=(i,)))
            self.assertContains(response, 'href="/coaches/2/"')


       