from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class TestBooks(TestCase):
    def test_BOOK_list_page_status_code(self):
        url = reverse('bookstore')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_BOOK_list_page_template(self):
        url = reverse('bookstore')
        response = self.client.get(url)
        self.assertTemplateUsed(response, "_base.html")
