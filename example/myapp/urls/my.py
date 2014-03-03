from myapp.models import Beta, Gamma
from myapp import forms
from django.conf.urls import patterns
from urlmagic.my import MyUrlGenerator


urlpatterns = patterns(
    "",
    MyUrlGenerator.add(Beta, form_class=forms.MyBetaAdd),
    MyUrlGenerator.edit(Beta, form_class=forms.MyBetaEdit),
    MyUrlGenerator.list(Beta),
    MyUrlGenerator.detail(Beta),
    MyUrlGenerator.delete(Beta),
    MyUrlGenerator.singular_add(Gamma),
    MyUrlGenerator.singular_detail(Gamma),
    MyUrlGenerator.singular_edit(Gamma),
    MyUrlGenerator.singular_delete(Gamma),
)
