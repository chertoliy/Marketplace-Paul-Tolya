from django.urls import reverse_lazy
from django.views.generic import ListView
from .models import TheShops


class HomeListView(ListView):
    model = TheShops
    template_name = 'app_market/main.html'
