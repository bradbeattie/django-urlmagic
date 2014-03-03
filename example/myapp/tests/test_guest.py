from django.core.urlresolvers import reverse
from myapp.tests import common


class GuestTest(common.CommonTestClass):

    def setUp(self):
        super(GuestTest, self).setUp()
        self.establish_guest_client()

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
                print "Guest", reverse(name, args=args), pattern.name,
                response = self.client.get(reverse(name, args=args))
                if name.startswith("admin:"):
                    self.assertEqual(response.status_code, 200)
                    self.assert_("login-form" in response.content)
                    print "Login form"
                elif pattern.name.startswith((
                    "staff_",
                    "member_",
                    "my_",
                )):
                    self.assertEqual(response.status_code, 302)
                    print 302
                else:
                    self.assertEqual(response.status_code, 200)
                    print 200
