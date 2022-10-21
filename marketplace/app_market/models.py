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


class PromoEvents(models.Model):
    id = models.AutoField(primary_key=True)
    shop = models.ForeignKey(TheShops, on_delete=models.CASCADE, verbose_name=_("The shop"),
                             blank=True, null=True)
    event_title = models.CharField(verbose_name=_("Event title"), max_length=100, null=True, blank=True)
    event_text = models.CharField(verbose_name=_("Event text"), max_length=100, null=True, blank=True)
    create_date = models.DateTimeField(auto_now=True, verbose_name=_("Time of creation event"))
    active = models.BooleanField(verbose_name=_("Activity status"), default=False)

    def __str__(self):
        return f"{self.event_title}"

    class Meta:
        db_table = 'events'
        verbose_name = _("Event")
        verbose_name_plural = _("Events")
        ordering = ['-create_date']


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    shop = models.ForeignKey(TheShops, on_delete=models.CASCADE, verbose_name=_("The shop"),
                             blank=True, null=True)
    name = models.CharField(verbose_name=_("Product"), max_length=12, null=True, blank=True)
    text = models.TextField(verbose_name=_("Product description"))
    cost = models.FloatField(verbose_name=_("Cost of the product"))
    create_date = models.DateTimeField(auto_now=True, verbose_name=_("Time of creation product"))

    def __str__(self):
        return f"{self.name} - {self.shop.name}"

    class Meta:
        db_table = 'products'
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ['id']
