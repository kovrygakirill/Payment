from core.test import TestCaseDB
from business_logic.my_exceptions import NotValidUserProfile, NotValidTINsForSend
from business_logic.logic_payment.profile_user import get_user_profile_by_id, get_users_profile_by_tin


class TestProfileUser(TestCaseDB):
    '''python manage.py test tests.test_profile_user --settings=config.settings.test'''

    def test_get_user_profile_by_id_correct_user(self):
        u_id = 1
        result = str(get_user_profile_by_id(user_id=u_id))
        expect = "POP"
        self.assertEqual(result, expect)

    def test_get_user_profile_by_id_not_exist_user(self):
        u_id = 300
        self.assertRaises(NotValidUserProfile, get_user_profile_by_id, user_id=u_id)

    def test_get_user_profile_by_id_not_correct_type_id(self):
        u_id = "3f"
        self.assertRaises(ValueError, get_user_profile_by_id, user_id=u_id)

    def test_get_user_profile_by_id_type_id_is_none(self):
        u_id = None
        self.assertRaises(NotValidUserProfile, get_user_profile_by_id, user_id=u_id)

    def test_get_users_profile_by_tin_correct(self):
        tins = [user.tin for user in self.users_profile]
        result = set(get_users_profile_by_tin(tins=tins))
        expect = set(self.users_profile)
        self.assertEqual(result, expect)

    def test_get_users_profile_by_tin_not_exist_tins(self):
        tins = ["0b9a8dc971be4768aeed3811ed11dd62", "129a8dc978be4768aeed3811ed31dd62"]
        result = list(get_users_profile_by_tin(tins))
        expect = []
        self.assertEqual(result, expect)

    def test_get_users_profile_by_tin_not_correct_format_tins(self):
        tins = ["dsvfdsv", "1"]
        self.assertRaises(NotValidTINsForSend, get_users_profile_by_tin, tins=tins)

    def test_get_users_profile_by_tin_tins_is_none(self):
        tins = None
        self.assertRaises(TypeError, get_users_profile_by_tin, tins=tins)
