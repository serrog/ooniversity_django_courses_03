from django.core.urlresolvers import resolve, reverse
from django.test import TestCase
from datetime import date
from django.test import Client
from students.models import Student
from courses.models import Course
from students.views import StudentListView, StudentDetailView

def create_students():
    course1 = Course.objects.create(
        name = 'course1', 
        short_description = 'short description 1',
        description = 'description 1'
    )
    course2 = Course.objects.create(
        name = 'course2', 
        short_description = 'short description 2',
        description = 'description 2'
    )
    course3 = Course.objects.create(
        name = 'course3', 
        short_description = 'short description 3',
        description = 'description 3'
    )
    students1 = Student.objects.create(
        name = 'Name1',
        surname = 'Surname1',
        date_of_birth = date.today(),
        email = 'email1@ex.com',
        phone = '123456',
        address = 'Adress1',
        skype = 'Skype1'
    )
    students1.courses.add(course1)
    students2 = Student.objects.create(
        name = 'Name2',
        surname = 'Surname2',
        date_of_birth = date.today(),
        email = 'email2@ex.com',
        phone = '123456',
        address = 'Adress2',
        skype = 'Skype2'
    )
    students2.courses.add(course3)
    students3 = Student.objects.create(
        name = 'Name3',
        surname = 'Surname3',
        date_of_birth = date.today(),
        email = 'email3@ex.com',
        phone = '123456',
        address = 'Adress3',
        skype = 'Skype3'
    )
    students3.courses.add(course3)


class StudentsListTest(TestCase):

    def test_student_list_url_resolves_to_list_page(self):
        self.assertEqual(resolve(
            '/students/').func.__name__, 
            StudentListView.as_view().__name__
        )

    def test_student_list_view_render_wright_template(self):
        client = Client()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'students/student_list.html')

    def test_rendered_correct_html(self):
        client = Client()
        response = client.get('/students/')
        self.assertContains(response, "<h2>Student's list</h2>")
        self.assertContains(response, '<th>Name</th>')
        self.assertContains(response, '<th>Name</th>')
        self.assertContains(response, '<th>Address</th>')
        self.assertContains(response, '<th>Skype</th>')


    def test_student_list_response_contains_correct_context(self):
        client = Client()
        create_students()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 2)
        for i, student in enumerate(response.context['object_list']):
            self.assertEqual(student.name, 'Name{}'.format(i+1))
            self.assertEqual(student.surname, 'Surname{}'.format(i+1))
            self.assertEqual(student.email, 'email{}@ex.com'.format(i+1))
            self.assertEqual(student.skype, 'Skype{}'.format(i+1))

    def test_student_list_response_contains_correct_context_for_one_course(self):
        client = Client()
        create_students()
        response = client.get('/students/?course_id=3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 2)
        for i, student in enumerate(response.context['object_list']):
            self.assertEqual(student.name, 'Name{}'.format(i+2))
            self.assertEqual(student.surname, 'Surname{}'.format(i+2))
            self.assertEqual(student.email, 'email{}@ex.com'.format(i+2))
            self.assertEqual(student.skype, 'Skype{}'.format(i+2))

    def test_student_list_template_contains_correct_links_to_edit_student(self):
        client = Client()
        create_students()
        response = client.get('/students/')
        for i in range(1, 3):
            self.assertContains(response, 'href="/students/edit/{}/"'.format(i))

    def test_student_list_template_contains_correct_links_to_delete_students(self):
        client = Client()
        create_students()
        response = client.get('/students/')
        for i in range(1, 3):
            self.assertContains(response, 'href="/students/remove/{}/"'.format(i))

    def test_student_list_template_contains_correct_links_to_add_student(self):
        client = Client()
        response = client.get('/students/')
        self.assertContains(response, 'href="/students/add/"')



class StudentsDetailTest(TestCase):

    def test_detail_url_resolves_to_detail_page(self):
        create_students()
        for i in range(1, 4):
            self.assertEqual(
                resolve('/students/{}/'.format(i)).func.__name__, 
                StudentDetailView.as_view().__name__
            )

    def test_detail_view_not_render_wright_template_with_non_existing_student(self):
        client = Client()
        response = client.get(reverse('students:detail', args=(1, )))
        self.assertEqual(response.status_code, 404)

    def test_detail_view_render_wright_template(self):
        create_students()
        client = Client()
        for i in range(1, 4):
            response = client.get(reverse('students:detail', args=(i,)))
            self.assertEqual(response.status_code, 200)

    def test_rendered_correct_html(self):
        client = Client()
        create_students()
        response = client.get(reverse('students:detail', args=(1,)))
        self.assertTemplateUsed(response, 'students/student_detail.html')
        self.assertContains(response, '<h2>Name1 Surname1</h2>')

    def test_student_detail_response_contains_correct_context(self):
        client = Client()
        create_students()
        for i in range(1, 4):
            response = client.get(reverse('students:detail', args=(i,)))
            student = response.context['object']
            self.assertEqual(student.name, 'Name{}'.format(i))
            self.assertEqual(student.surname, 'Surname{}'.format(i))
            self.assertEqual(student.email, 'email{}@ex.com'.format(i))
            self.assertEqual(student.skype, 'Skype{}'.format(i))

    def test_student_detail_template_contains_link_to_courses(self):
        client = Client()
        create_students()
        response = client.get(reverse('students:detail', args=(1,)))
        self.assertContains(response, 'href="/courses/1/"')

    