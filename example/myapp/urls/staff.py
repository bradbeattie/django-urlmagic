from myapp.models import Alpha, Beta, Gamma, Delta, Epsilon
from django.conf.urls import patterns
from urlmagic.staff import StaffUrlGenerator


urlpatterns = patterns("")


for model in (Alpha, Beta, Gamma, Delta, Epsilon):
    urlpatterns += patterns(
        "",
        StaffUrlGenerator.add(model),
        StaffUrlGenerator.edit(model),
        StaffUrlGenerator.list(model),
        StaffUrlGenerator.detail(model),
        StaffUrlGenerator.delete(model),
    )
