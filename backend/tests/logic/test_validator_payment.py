from decimal import Decimal
from core.test import BaseTestCase
from business_logic.logic_payment.validator import ValidatorPayment
from business_logic.my_exceptions import NotValidMoneyForSend


class TestValidatorPayment(BaseTestCase):
    '''python manage.py test tests.test_validator_payment --settings=config.settings.test'''

    @classmethod
    def setUpClass(cls):
        cls.val = ValidatorPayment()

    def test_convert_to_list_recipients_string_empty(self):
        data = ""
        result = self.val.convert_to_list_recipients(data)
        expect_result = []
        self.assertEqual(result, expect_result)

    def test_convert_to_list_recipients_string_with_one_tin(self):
        data = "123"
        result = self.val.convert_to_list_recipients(data)
        expect_result = ['123']
        self.assertEqual(result, expect_result)

    def test_convert_to_list_recipients_string_correct(self):
        data = "123 234 345"
        result = self.val.convert_to_list_recipients(data)
        expect_result = ['123', '234', '345']
        self.assertEqual(result, expect_result)

    def test_convert_to_list_recipients_string_with_negative_gaps(self):
        data = " 123    234  345"
        result = self.val.convert_to_list_recipients(data)
        expect_result = ['123', '234', '345']
        self.assertEqual(result, expect_result)

    def test_convert_to_list_recipients_string_is_None(self):
        data = None
        self.assertRaises(AttributeError, self.val.convert_to_list_recipients, recipients=data)

    def test_convert_to_list_recipients_string_is_number(self):
        data = 1223
        self.assertRaises(AttributeError, self.val.convert_to_list_recipients, recipients=data)

    def test_check_money_correct(self):
        money = Decimal(20)
        self.assertEqual(money, self.val.check_valid_money(money=money))

    def test_check_money_negative_value(self):
        money = Decimal(-10)
        self.assertRaises(NotValidMoneyForSend, self.val.check_valid_money, money=money)

    def test_check_money_zero_value(self):
        money = Decimal(0)
        self.assertRaises(NotValidMoneyForSend, self.val.check_valid_money, money=money)
