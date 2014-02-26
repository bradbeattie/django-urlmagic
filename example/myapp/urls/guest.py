from myapp.models import Alpha, Beta, Gamma
from django.conf.urls import patterns
from urlmagic.guest import GuestUrlGenerator


urlpatterns = patterns("")


for model in (Alpha, Beta, Gamma):
    urlpatterns += patterns(
        "",
        GuestUrlGenerator.add(model),
        GuestUrlGenerator.edit(model),
        GuestUrlGenerator.list(model),
        GuestUrlGenerator.detail(model),
        GuestUrlGenerator.delete(model),
    )
