from django.core.exceptions import ValidationError

from users.models import UserProfile
from business_logic.my_exceptions import NotValidUserProfile, NotValidTINsForSend


def get_user_profile_by_id(user_id: int) -> UserProfile:
    try:
        return UserProfile.objects.select_related("user").get(user__pk=user_id)
    except UserProfile.DoesNotExist:
        raise NotValidUserProfile(f"UserProfile don't exist with user_id {user_id}")


def get_users_profile_by_tin(tins: list) -> list[UserProfile]:
    try:
        return UserProfile.objects.select_related("user").filter(tin__in=tins)
    except ValidationError:
        raise NotValidTINsForSend("Not valid format(tins)")
