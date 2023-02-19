from django.test import Client

from users.models import UserProfile
from core.test import TestCaseDB


class TestPayment(TestCaseDB):
    '''python manage.py test tests.test_view_payment --settings=config.settings.test'''

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()

    def test_make_payment_url_exists_at_desired_location(self):
        response = self.client.post('/payments/user/2/')
        self.assertEqual(response.status_code, 200)

    def test_make_payment_correct(self):
        user_to = self.users_profile[0]  # balance = 10
        user_from = self.users_profile[1]  # balance 20
        response = self.client.post(path='/payments/user/2/', data={'tins': user_to.tin, 'money': 2})
        self.assertEqual(response.status_code, 200)
        expect = {12, 18}
        updated_user = UserProfile.objects.select_related('user').filter(tin__in=[user_to.tin, user_from.tin])
        result = {int(updated_user[0].balance), int(updated_user[1].balance)}
        self.assertEqual(result, expect)

    def test_make_payment_not_enough_balance(self):
        user_to = self.users_profile[0]  # balance = 10
        response = self.client.post(path='/payments/user/2/', data={'tins': user_to.tin, 'money': 500})
        self.assertEqual(response.status_code, 200)
        expect = {'error': 'Not enough balance to transfer'}
        result = response.data
        self.assertEqual(result, expect)

    def test_make_payment_not_correct_tins(self):
        response = self.client.post(path='/payments/user/2/', data={'tins': "", 'money': 5})
        self.assertEqual(response.status_code, 200)
        expect = {'error': {'tins': ['This field is required.']}}
        result = response.data
        self.assertEqual(result, expect)

    def test_make_payment_not_correct_length_tins(self):
        response = self.client.post(path='/payments/user/2/', data={'tins': "sdcsdc", 'money': 5})
        self.assertEqual(response.status_code, 200)
        expect = {'error': {'tins': ['Ensure this value has at least 32 characters (it has 6).']}}
        result = response.data
        self.assertEqual(result, expect)

    def test_make_payment_negative_money(self):
        user_to = self.users_profile[0]  # balance = 10
        response = self.client.post(path='/payments/user/2/', data={'tins': user_to.tin, 'money': -1})
        self.assertEqual(response.status_code, 200)
        expect = {'error': 'Money could not be negative or zero for send'}
        result = response.data
        self.assertEqual(result, expect)

    def test_make_payment_not_exist_tins(self):
        response = self.client.post(path='/payments/user/2/',
                                    data={'tins': "b1f24d3ebc8945ec1001f261b6ef0639", 'money': 5})
        self.assertEqual(response.status_code, 200)
        expect = {'error': 'This tins dont exist'}
        result = response.data
        self.assertEqual(result, expect)

    def test_make_payment_not_valid_format_tins(self):
        response = self.client.post(path='/payments/user/2/',
                                    data={'tins': '[11f24d3ebc8945ec8001f261b6ef0639]', 'money': 5})
        self.assertEqual(response.status_code, 200)
        expect = {'error': 'Not valid format(tins)'}
        result = response.data
        self.assertEqual(result, expect)
