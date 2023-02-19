from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from decimal import Decimal

from .forms import PaymentForm
from business_logic.logic_payment.payment import make_payment
from business_logic.logic_payment.profile_user import get_user_profile_by_id, get_users_profile_by_tin
from business_logic.logic_payment.validator import ValidatorPayment
from business_logic.my_exceptions import MyException


class PaymentsViewSet(viewsets.ViewSet):
    validator = ValidatorPayment()

    def make_payment(self, request: Request, id: int):
        form = PaymentForm(request.POST)
        if form.is_valid():
            try:
                recipients: str = form.cleaned_data["tins"]
                money: Decimal = form.cleaned_data["money"]
                recipients_list = self.validator.convert_to_list_recipients(recipients=recipients)
                money = self.validator.check_valid_money(money=money)

                user_sender = get_user_profile_by_id(user_id=id)
                users_recipients = get_users_profile_by_tin(tins=recipients_list)

                make_payment(user_from=user_sender, users_to=users_recipients, money=money)

                response = Response({"success": 1})
            except MyException as me:
                response = Response({"error": me.message})
        else:
            response = Response({"error": form.errors})

        return response
