from django.test import TestCase

from django.test import RequestFactory
from .views import cadastro

# Create your tests here.

class cadastroTest(TestCase):
    def test_cadastro(self):
        
        request = RequestFactory().get('/cadastro')
        response = cadastro(request)
        self.assertEqual(response.status_code, 200)
    def test_string(self):

        self.assertGreater(self.len(),5)



