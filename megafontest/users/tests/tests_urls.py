from django.test import SimpleTestCase
from django.urls import resolve, reverse

class Urls(SimpleTestCase):
    def test_detail_url(self):
        path = reverse('token')
        print(resolve(url))