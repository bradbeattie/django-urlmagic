from myapp.models import Alpha, Beta, Gamma
from django.conf.urls import patterns
from urlmagic.staff import StaffUrlGenerator


urlpatterns = patterns("")


for model in (Alpha, Beta, Gamma):
    urlpatterns += patterns(
        "",
        StaffUrlGenerator.list(model),
        StaffUrlGenerator.add(model),
        StaffUrlGenerator.edit(model),
        StaffUrlGenerator.delete(model),
        StaffUrlGenerator.detail(model),
    )
