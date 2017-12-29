import factory
from django.test import TestCase

from auth0authorization import models


class Auth0LoginProfileFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Auth0LoginProfile
        django_get_or_create = ('user',)


# class AccountsModelsTests(TestCase):
#     def setUp(self):
#         self.email = 'test@test.com'
#         self.user = UserFactory.create(email=self.email, username=self.email)

#     def test_unicode(self):
#         self.assertEqual(str(self.user), self.email)

#     def test_super_user(self):
#         super_user = User.objects.create_superuser(
#             username='email@test.com',
#             email='email@test.com',
#             password='123456'
#         )
#         self.assertEqual(super_user.is_superuser, True)

#     def test_user(self):
#         user = User.objects.create_user(email='email@test.com',
#                                         first_name='user',
#                                         last_name='test',
#                                         password='test',
#                                         username='email@test'
#                                         )
#         self.assertEqual(user.is_superuser, False)

#     def test_get_full_name(self):
#         self.assertEqual(self.user.get_full_name(), 'John Doe')

#     def test_get_short_name(self):
#         self.assertEqual(self.user.get_short_name(), 'John')
