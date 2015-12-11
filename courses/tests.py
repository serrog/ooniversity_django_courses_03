from django.test import TestCase
from django.test import Client
from courses.models import Course

class CoursesListTest(TestCase):

	def test_index_page_without_courses(self):
		client = Client()
		response = client.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'index.html')

	def test_index_page_with_courses(self):
		client = Client()
		course1 = Course.create(
			'name': 'course1', 
			'short_description': 'short description 1',
			'description': 'description 1'
		)
		course2 = Course.create(
			'name': 'course2', 
			'short_description': 'short description 2',
			'description': 'description 2'
		)
		response = client.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'index.html')
		self.assertEqual(len(response.context['all_courses']), 2)


		assertContains(response, text, count=None, status_code=200, msg_prefix='', html=False)

