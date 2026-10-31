from django.test import SimpleTestCase
from django.urls import resolve, reverse


class HomeViewTests(SimpleTestCase):
    def test_home_page_returns_success(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, World!")
        self.assertContains(response, "Welcome to the Django application.")

    def test_home_url_resolves_to_home_view(self):
        match = resolve(reverse("home"))

        self.assertEqual(match.url_name, "home")
        self.assertEqual(match.func.__name__, "home")


class AboutViewTests(SimpleTestCase):
    def test_about_page_returns_success(self):
        response = self.client.get(reverse("about"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "About Page")
        self.assertContains(response, "This is the about page of the Django application.")

    def test_about_url_resolves_to_about_view(self):
        match = resolve(reverse("about"))

        self.assertEqual(match.url_name, "about")
        self.assertEqual(match.func.__name__, "about")

