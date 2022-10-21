from django.urls import path

from .views import ProfileLogoutView, RegisterUserView, ProfileLoginView, ProfileUpdateView

urlpatterns = [
    path('login', ProfileLoginView.as_view(), name='login'),
    path('logout', ProfileLogoutView.as_view(), name='logout'),
    path('register', RegisterUserView.as_view(), name='register'),
    path('profile/<int:pk>', ProfileUpdateView.as_view(), name='profile')
]