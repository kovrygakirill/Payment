from django.test import Client

from core.test import TestCaseDB


class TestUserViewSet(TestCaseDB):
    '''python manage.py test tests.test_view_users --settings=config.settings.test'''

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()

    def setUp(self):
        self.response = self.client.get('/users/')

    def test_get_all_users_url_exists_at_desired_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_get_all_users_correct(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(len(self.response.data), 3)
