from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserProfile(AbstractUser):
    balance = models.FloatField(verbose_name=_("Balance"), default=0)
    city = models.CharField(verbose_name=_("City"), max_length=36, blank=True)
    phone_number = models.CharField(verbose_name=_("Phone number"), max_length=12, null=True, blank=True)
    date_of_birthday = models.DateField(verbose_name=_("Date of birth"), null=True, blank=True)
    groups = models.ForeignKey(Group, blank=True, null=True, on_delete=models.CASCADE, verbose_name=_("Group"))

    def __str__(self):
        return f"{self.username}"

    class Meta:
        db_table = 'user_profile'
        verbose_name = _("User profile")
        verbose_name_plural = _("User profiles")
        ordering = ['username']
