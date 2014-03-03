from myapp.models import Alpha, Beta, Gamma
from django.conf.urls import patterns
from urlmagic.member import MemberUrlGenerator


urlpatterns = patterns("")


for model in (Alpha, Beta, Gamma):
    urlpatterns += patterns(
        "",
        MemberUrlGenerator.list(model),
        MemberUrlGenerator.add(model),
        MemberUrlGenerator.edit(model),
        MemberUrlGenerator.delete(model),
        MemberUrlGenerator.detail(model),
    )
