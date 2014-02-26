from urlmagic.core import MemberUrlGenerator
from django.contrib.auth.decorators import user_passes_test


class SuperuserUrlGenerator(MemberUrlGenerator):

    @classmethod
    def adjust_dict(cls, d):
        d.setdefault("format_kwargs", {})
        d["format_kwargs"].setdefault("role", "superuser")
        super(SuperuserUrlGenerator, cls).adjust_dict(d)
        return d

    @classmethod
    def adjust_result(cls, r):
        super(SuperuserUrlGenerator, cls).adjust_result(r)
        r._callback = user_passes_test(lambda u: u.is_superuser)(r._callback)
        return r
