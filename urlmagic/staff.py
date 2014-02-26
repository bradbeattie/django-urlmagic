from urlmagic.member import MemberUrlGenerator
from django.contrib.auth.decorators import user_passes_test


class StaffUrlGenerator(MemberUrlGenerator):

    @classmethod
    def adjust_dict(cls, d):
        d.setdefault("format_kwargs", {})
        d.setdefault("permission_format", True)
        d["format_kwargs"].setdefault("role", "staff")
        super(StaffUrlGenerator, cls).adjust_dict(d)
        return d

    @classmethod
    def adjust_result(cls, r):
        super(StaffUrlGenerator, cls).adjust_result(r)
        r._callback = user_passes_test(lambda u: u.is_staff)(r._callback)
        return r
