from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import home_view, redirect_url_view


class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home_view)

    def test_redirect_url_is_resolved(self):
        url = reverse('redirect', args=['some-str'])
        self.assertEquals(resolve(url).func, redirect_url_view)
