from myapp.models import Alpha, Beta, Gamma, Delta, Epsilon
from django.conf.urls import patterns
from urlmagic import member


urlpatterns = patterns("")


for model in (Alpha, Beta, Gamma, Delta, Epsilon):
    urlpatterns += patterns(
        "",
        member.get_add_url(model),
        member.get_edit_url(model),
        member.get_list_url(model),
        member.get_detail_url(model),
        member.get_delete_url(model),
        member.get_list_url(model),
    )
