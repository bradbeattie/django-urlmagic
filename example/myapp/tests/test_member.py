from django.core.urlresolvers import reverse
from myapp import models
from myapp.tests import common


class MemberTest(common.CommonTestClass):

    def setUp(self):
        super(MemberTest, self).setUp()
        self.establish_member_client()

    def url_test(self, patterns, namespaces=[]):
        for pattern in patterns:
            if hasattr(pattern, "url_patterns"):
                self.url_test(
                    pattern.url_patterns,
                    namespaces + (["%s" % pattern.namespace] if pattern.namespace else []),
                )
            elif pattern.name:
                args = []
                name = ":".join(namespaces + [pattern.name])
                if "(?P<pk>" in pattern.regex.pattern:
                    args.append(1)
                elif "(" in pattern.regex.pattern or pattern.name.startswith(("logout", "django-admin")):
                    continue
                print "Member", reverse(name, args=args), pattern.name,
                response = self.client.get(reverse(name, args=args))
                if pattern.name.startswith((
                    "staff_",
                    "my_gamma_add",
                )):
                    self.assertEqual(response.status_code, 302)
                    print 302
                elif name.startswith("admin:"):
                    self.assertEqual(response.status_code, 200)
                    self.assert_("login-form" in response.content)
                    print "Login form"
                else:
                    self.assertEqual(response.status_code, 200)
                    print 200

    # Confirm that an owned object gets saved with the right owner
    def test_submit_owned_object(self):
        slug = "test_submit_owned_object_slug"
        name = "Test Submit Owned Object Name"
        self.assertEqual(models.Beta.objects.filter(slug=slug).count(), 0)
        self.client.post(reverse("my_beta_add"), {"name": name, "slug": slug})
        self.assertEqual(self.client.user, models.Beta.objects.get(slug=slug, name=name).owner)
