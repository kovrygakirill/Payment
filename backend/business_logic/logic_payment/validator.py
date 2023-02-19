from decimal import Decimal

from business_logic.my_exceptions import NotValidMoneyForSend


class ValidatorPayment:
    def convert_to_list_recipients(self, recipients: str) -> list:
        return recipients.split()

    def check_valid_money(self, money: Decimal) -> Decimal:
        if money > 0:
            return money
        raise NotValidMoneyForSend('Money could not be negative or zero for send')
