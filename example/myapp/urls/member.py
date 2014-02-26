from myapp.models import Alpha, Beta, Gamma, Delta, Epsilon
from django.conf.urls import patterns
from urlmagic.member import MemberUrlGenerator


urlpatterns = patterns("")


for model in (Alpha, Beta, Gamma, Delta, Epsilon):
    urlpatterns += patterns(
        "",
        MemberUrlGenerator.add(model),
        MemberUrlGenerator.edit(model),
        MemberUrlGenerator.list(model),
        MemberUrlGenerator.detail(model),
        MemberUrlGenerator.delete(model),
        MemberUrlGenerator.list(model),
    )
