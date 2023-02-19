from django.urls import path

from .views import UserViewSet

users = UserViewSet.as_view({
    'get': 'get_all_users'
})

urlpatterns = [
    path(r'', users, name='users'),
]
