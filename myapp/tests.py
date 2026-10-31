from django.test import TestCase


class HealthTests(TestCase):
    def test_health_status_code(self):
        response = self.client.get('/health/')
        self.assertEqual(response.status_code, 200)

    def test_health_body(self):
        response = self.client.get('/health/')
        self.assertEqual(response.json()["status"], "ok")