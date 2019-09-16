from django.test import SimpleTestCase
from django.urls import resolve, reverse

class Urls(SimpleTestCase):
    def test_detail_url_one(self):
        path_one = reverse('token')
        print(resolve(path))
    
     def test_detail_url_two(self):
        path_two = reverse('token')
        print(resolve(path))