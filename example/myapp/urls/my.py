from myapp.models import Beta, Gamma, Delta
from django.conf.urls import patterns
from urlmagic.my import MyUrlGenerator


urlpatterns = patterns("")


for model in (Beta, Gamma):
    urlpatterns += patterns(
        "",
        MyUrlGenerator.add(model),
        MyUrlGenerator.edit(model),
        MyUrlGenerator.list(model),
        MyUrlGenerator.detail(model),
        MyUrlGenerator.delete(model),
    )

urlpatterns += patterns(
    "",
    MyUrlGenerator.singular_add(Delta),
    MyUrlGenerator.singular_detail(Delta),
    MyUrlGenerator.singular_edit(Delta),
    MyUrlGenerator.singular_delete(Delta),
)
