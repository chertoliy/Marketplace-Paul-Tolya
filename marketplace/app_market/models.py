from django.db import models
from django.utils.translation import gettext_lazy as _


class TheShops(models.Model):
    id = models.AutoField(primary_key=True)
    create_date = models.DateTimeField(auto_now=True, verbose_name=_("Shop create time"))
    name = models.CharField(max_length=200, verbose_name=_("Name of the shop"))
    text = models.TextField(verbose_name=_("Content of the shop"))
    update_date = models.DateTimeField(auto_now=True, verbose_name=_("Shop update time"))
    verification = models.BooleanField(default=False, verbose_name=_("Verification status of shop"))

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'the_shops'
        verbose_name = _("The shop")
        verbose_name_plural = _("The shops")
        ordering = ['id']
