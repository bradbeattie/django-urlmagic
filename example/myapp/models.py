from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from myapp.base_models import NamedAndSlugged, MightHaveOwner


class Alpha(NamedAndSlugged):
    def get_absolute_url(self):
        return reverse("guest_alpha_detail", args=[self.slug])


class Beta(NamedAndSlugged, MightHaveOwner):
    def get_absolute_url(self):
        return reverse("guest_beta_detail", args=[self.slug])


class Gamma(models.Model):
    owner = models.OneToOneField(User, db_index=True)
    name = models.CharField(max_length=100, db_index=True)
    def get_absolute_url(self):
        return reverse("guest_gamma_detail", args=[self.pk])
    class Meta:
        verbose_name = "Verbose-named Gamma"
