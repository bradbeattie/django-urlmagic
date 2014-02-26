from myapp.models import Beta, Gamma, Delta
from django.conf.urls import patterns
from urlmagic import my


urlpatterns = patterns("")


for model in (Beta, Gamma):
    urlpatterns += patterns(
        "",
        my.get_add_url(model),
        my.get_edit_url(model),
        my.get_list_url(model),
        my.get_detail_url(model),
        my.get_delete_url(model),
        my.get_list_url(model),
    )

urlpatterns += patterns(
    "",
    my.get_singular_add_url(Delta),
    my.get_singular_detail_url(Delta),
    my.get_singular_edit_url(Delta),
    my.get_singular_delete_url(Delta),
)
