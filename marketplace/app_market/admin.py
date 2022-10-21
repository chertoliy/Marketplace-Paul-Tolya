from django.contrib import admin
from .models import TheShops, Products, PromoEvents
from django.utils.translation import gettext_lazy as _


@admin.register(TheShops)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'get_truncated_text', 'create_date', 'verification']
    list_display_links = ['id', 'name', 'get_truncated_text']
    list_filter = ['name']
    actions = ['activate', 'deactivate', 'add_markets']

    def activate(self, request, queryset):
        queryset.update(verification=True)

    def deactivate(self, request, queryset):
        queryset.update(verification=False)

    def get_truncated_text(self, obj):
        return f"{obj.text[:15]}..."

    def add_markets(self, request, queryset):
        for i in range(100):
            TheShops.objects.create(
                name=f"Магазин {i}",
                text=f"Описание {i}",
                verification=True
            )

    get_truncated_text.short_description = _("Truncated content")
    activate.short_description = _("Verify the shop")
    deactivate.short_description = _("Remove the shop verification")


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'shop', 'create_date']
    list_display_links = ['id', 'name']
    actions = ['add_products']

    def add_products(self, request, queryset):
        for i in range(100):
            Products.objects.create(
                name=f"Продукт {i}",
                text=f"Описание {i}",
                cost=1234,
                shop=TheShops.objects.get(id=1)

            )


@admin.register(PromoEvents)
class PromoEventsAdmin(admin.ModelAdmin):
    list_display = ['id', 'event_title', 'shop', 'create_date', 'active']
    list_display_links = ['id', 'event_title']
    actions = ['add_promo']

    def add_promo(self, request, queryset):
        for i in range(100):
            PromoEvents.objects.create(
                shop=TheShops.objects.get(id=1),
                event_title=f"Event {i}",
                event_text=f"Event {i}",
                active=True
            )

