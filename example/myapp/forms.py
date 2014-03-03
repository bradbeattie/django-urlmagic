from django import forms
from myapp import models
from urlmagic.mixins import AutomaticUserFormMixin


class MyBetaAdd(AutomaticUserFormMixin, forms.ModelForm):
    class Meta:
        model = models.Beta
        exclude = ["owner"]


class MyBetaEdit(forms.ModelForm):
    class Meta:
        model = models.Beta
        exclude = ["owner"]
