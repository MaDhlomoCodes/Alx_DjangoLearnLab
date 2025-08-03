from django.test import TestCase
from django.urls import reverse

class SecurityTests(TestCase):
    def test_csrf_protection(self):
        response = self.client.post(reverse('book_create'))
        self.assertEqual(response.status_code, 403)  # Should block without CSRF

    def test_xss_protection(self):
        response = self.client.get('/?q=<script>alert(1)</script>')
        self.assertNotIn(b'<script>', response.content)