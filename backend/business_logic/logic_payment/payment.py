from decimal import Decimal
from django.db import transaction, DatabaseError

from users.models import UserProfile
from business_logic.my_exceptions import LackOfBalance, NotValidTINsForSend, ProblemWithDataBase


def make_payment(user_from: UserProfile, users_to: list[UserProfile], money: Decimal) -> None:
    if not users_to:
        raise NotValidTINsForSend("This tins dont exist")

    if user_from.balance >= money:
        money_for_each = money / len(users_to)

        try:
            with transaction.atomic():
                user_from.balance -= money
                user_bulk_update_list = [user_from]
                for user_to in users_to:
                    user_to.balance += money_for_each
                    user_bulk_update_list.append(user_to)
                UserProfile.objects.bulk_update(user_bulk_update_list, ['balance'])
        except DatabaseError:
            raise ProblemWithDataBase("Payment failed. Database have problems!")
    else:
        raise LackOfBalance("Not enough balance to transfer")
