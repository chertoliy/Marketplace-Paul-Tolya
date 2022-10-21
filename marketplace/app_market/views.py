from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import TheShops, Products, PromoEvents
from django.core.cache import cache


class HomeListView(ListView):
    model = TheShops
    template_name = 'app_market/main.html'
    paginate_by = 8

    def __init__(self):
        super().__init__()
        self.len_queryset = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        list_shops = TheShops.objects.filter(verification=True)
        paginator = Paginator(list_shops, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            file_shops = paginator.page(page)
        except PageNotAnInteger:
            file_shops = paginator.page(1)
        except EmptyPage:
            file_shops = paginator.page(paginator.num_pages)
        context['list_shops'] = file_shops
        return context


class ShopDetailView(DetailView):
    model = TheShops
    template_name = 'app_market/shop_page.html'
    context_object_name = 'get_shop'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        list_promo = cache.get_or_set(
            'list_promo_events',
            list(PromoEvents.objects.filter(shop__id=self.get_object().id, active=True)),
            60*30
        )
        if list_promo:
            context['main_event'], context['list_promo_events'] = list_promo.pop(0), list_promo
        else:
            context['main_event'], context['list_promo_events'] = None, None
        context['list_products'] = Products.objects.filter(shop__id=self.get_object().id)
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('shop_page', kwargs={'pk': self.get_object().id})
