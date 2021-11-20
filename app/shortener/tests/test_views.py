from django.test import TestCase, Client
from django.urls import reverse
from ..models import Shortener
from ..utils import create_random_code
import json


class TestViews(TestCase):

    def setUp(self):
        # creates a client that can send GET/POST requests to our server
        self.client = Client()
        # create reverse to home view
        self.home_url = reverse('home')
        # create new Short url object to google.com
        self.url1 = Shortener.objects.create(long_url='google.com')
        # create reverse to redirect view with the new short URL as an argument
        self.redirect = reverse('redirect', args=[self.url1.short_url])
        # creates non-existing short URL
        self.non_existing_url = create_random_code()
        self.redirect_non_existing = reverse('redirect', args=[self.non_existing_url])

    # testing home view
    # GET http://domain.com/
    # expecting to get a response with a home.html page and status code of 200
    def test_home_view_GET(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'shortener/home.html')

    # testing home view
    # POST http://domain.com/ with form that contains long_url
    # expecting to get a response with a new_url in the context and status code of 200
    def test_home_view_POST_create_new_short_url(self):
        response = self.client.post(
            '/',
            data={'long_url': 'https://geekflare.com/build-url-shortener-app-in-django/'},
        )
        self.assertEquals(response.status_code, 200)
        self.assertIsNotNone(response.context.get('new_url'))

    # testing redirect view
    # http://domain.com/<str:shortened_part>
    # expecting to get redirected to google.com and  status code of 302
    def test_redirect_view_GET(self):
        response = self.client.get(self.redirect)
        self.assertEquals(response.status_code, 302)
        self.assertEquals('google.com', response.url)

    # testing redirect view
    # http://domain.com/<non_existing shortened_part>
    # expecting to get HttpResponseNotFound and  status code of 404
    def test_non_existing_url(self):
        response = self.client.get(self.redirect_non_existing)
        self.assertEquals(response.status_code, 404)

