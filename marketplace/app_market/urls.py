from django.urls import path
from .views import HomeListView, ShopDetailView

urlpatterns = [
    path('', HomeListView.as_view(), name='home_page'),
    path('shop/<int:pk>', ShopDetailView.as_view(), name='shop'),
]
