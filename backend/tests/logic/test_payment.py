from decimal import Decimal

from core.test import TestCaseDB
from business_logic.my_exceptions import NotValidTINsForSend, LackOfBalance
from business_logic.logic_payment.payment import make_payment


class TestPayment(TestCaseDB):
    '''python manage.py test tests.test_payment --settings=config.settings.test'''

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_make_payment_correct(self):
        user_1_to = self.users_profile[0]  # balance - 10
        user_2_to = self.users_profile[1]  # balance - 20
        user_from = self.users_profile[2]  # balance - 30
        money = Decimal(20)
        make_payment(user_from=user_from, users_to=[user_1_to, user_2_to], money=money)
        result = [int(user_1_to.balance), int(user_2_to.balance), int(user_from.balance)]
        expect = [20, 30, 10]
        self.assertEqual(result, expect)

    def test_make_payment_not_enough_balance(self):
        user_1_to = self.users_profile[0]  # balance - 20
        user_2_to = self.users_profile[1]  # balance - 30
        user_from = self.users_profile[2]  # balance - 10
        money = Decimal(12)
        self.assertRaises(LackOfBalance, make_payment, user_from=user_from, users_to=[user_1_to, user_2_to],
                          money=money)

    def test_make_payment_have_not_users_to(self):
        user_from = self.users_profile[2]
        money = Decimal(5)
        self.assertRaises(NotValidTINsForSend, make_payment, user_from=user_from, users_to=[], money=money)
