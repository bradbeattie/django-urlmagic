from django.core.urlresolvers import reverse
from myapp.tests import common


class StaffTest(common.CommonTestClass):

    def setUp(self):
        super(StaffTest, self).setUp()
        self.establish_staff_client()

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
                print "Staff", reverse(name, args=args), pattern.name,
                response = self.client.get(reverse(name, args=args))
                if pattern.name.startswith("my_gamma_add", ):
                    self.assertEqual(response.status_code, 302)
                    print 302
                elif name.startswith("admin:") and pattern.name.startswith(("myapp_", "index", "password_", "jsi18n")):
                    self.assertEqual(response.status_code, 200)
                    print 200
                elif name.startswith("admin:"):
                    self.assertEqual(response.status_code, 403)
                    print 403
                else:
                    self.assertEqual(response.status_code, 200)
                    print 200
