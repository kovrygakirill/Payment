from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import UserProfileSerializer
from .models import UserProfile


class UserViewSet(viewsets.ViewSet):
    def get_all_users(self, request: Request):
        users = UserProfile.objects.select_related("user").all()
        serializer = UserProfileSerializer(users, many=True)
        return Response(data=serializer.data)
