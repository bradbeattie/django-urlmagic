from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from myapp.base_models import NamedAndSlugged, MustHaveOwner, MightHaveOwner


class Alpha(NamedAndSlugged):
    def get_absolute_url(self):
        return reverse("guest_alpha_detail", args=[self.slug])


class Beta(NamedAndSlugged, MightHaveOwner):
    def get_absolute_url(self):
        return reverse("guest_beta_detail", args=[self.slug])


class Gamma(NamedAndSlugged, MustHaveOwner):
    class Meta:
        verbose_name = "Verbose-named Gamma"
    def get_absolute_url(self):
        return reverse("guest_gamma_detail", args=[self.slug])


class Delta(NamedAndSlugged):
    owner = models.OneToOneField(User, db_index=True)
    def get_absolute_url(self):
        return reverse("guest_delta_detail", args=[self.slug])


class Epsilon(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def get_absolute_url(self):
        return reverse("guest_epsilon_detail", args=[self.pk])
    def __unicode__(self):
        return self.name
