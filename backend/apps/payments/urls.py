from django.urls import path
from .views import PaymentsViewSet

payment = PaymentsViewSet.as_view({
    'post': 'make_payment'
})

urlpatterns = [
    path(r'user/<int:u_id>/', payment, name='payment'),
]
