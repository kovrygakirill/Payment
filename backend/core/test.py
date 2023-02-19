import unittest
from decimal import Decimal
from django.db import connection

from users.models import UserProfile, User


class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


class TestCaseDB(BaseTestCase):
    @classmethod
    def setUpClass(cls):
        with connection.cursor() as cursor:
            cursor.execute("""UPDATE 'sqlite_sequence' SET seq = 0 WHERE name = 'auth_user';""")

        cls.users: User = User.objects.bulk_create([
            User(username="POP", email="pop@mail.ru", password="111"),
            User(username="TOT", email="tot@mail.ru", password="111"),
            User(username="Gosha", email="Gosha@mail.ru", password="111"),
        ])
        cls.users_profile: list[UserProfile] = UserProfile.objects.bulk_create([
            UserProfile(balance=Decimal(10), user=cls.users[0]),
            UserProfile(balance=Decimal(20), user=cls.users[1]),
            UserProfile(balance=Decimal(30), user=cls.users[2]),
        ])

    @classmethod
    def tearDownClass(cls):
        User.objects.all().delete()
        UserProfile.objects.all().delete()
