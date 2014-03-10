from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.models import Permission
from django.test import Client, TestCase
from django.utils.text import slugify
from example import urls


class CommonTestClass(TestCase):
    fixtures = ['test_data']

    def setUp(self):
        super(CommonTestClass, self).setUp()

    def generate_user(self, name):
        user, just_created = User.objects.get_or_create(
            username=slugify(unicode(name)),
            defaults={
                "first_name": name,
                "last_name": name,
                "email": "%s@example.com" % slugify(unicode(name)),
            },
        )
        if just_created:
            user.set_password("password")
            user.save()
        return user, just_created

    def establish_client(self, user):
        self.client = Client()
        self.client.user = user
        if not self.client.login(
            username=user.username,
            password="password",
        ):
            raise Exception("Failed to login")

    def establish_guest_client(self):
        self.client = Client()
        self.client.user = AnonymousUser()

    def establish_member_client(self):
        user, just_created = self.generate_user("Member")
        self.establish_client(user)

    def establish_staff_client(self):
        user, just_created = self.generate_user("Staff")
        if just_created:
            user.is_staff = True
            for permission in Permission.objects.all():
                user.user_permissions.add(permission)
            user.save()
        self.establish_client(user)

    def test_get_on_all_urls(self):
        self.url_test(urls.urlpatterns)
