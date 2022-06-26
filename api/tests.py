from django.test import TestCase
from .models import Book
class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Book.objects.create(title='first todo', body='a body here')
    def test_title_content(self):
        Book = Book.objects.get(id=1)
        expected_object_name = f'{book.title}'
        self.assertEqual(expected_object_name, 'first todo')
    def test_body_content(self):
        Book = Book.objects.get(id=1)
        expected_object_name = f'{book.author}'
        self.assertEqual(expected_object_name, 'a body here')
        

