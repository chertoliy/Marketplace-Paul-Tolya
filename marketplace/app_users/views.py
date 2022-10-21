from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .models import UserProfile, Purchases
from .forms import RegisterUserForm, AuthUserForm, EditProfileForm


class ProfileLogoutView(LogoutView):
    next_page = reverse_lazy('home_page')


class ProfileLoginView(LoginView):
    template_name = 'app_users/login_page.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('home_page')

    def get_success_url(self):
        return self.success_url


class RegisterUserView(CreateView):
    model = UserProfile
    template_name = 'app_users/register_page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('home_page')

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username, password=password)
        login(self.request, aut_user)
        return form_valid


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = UserProfile
    template_name = 'app_users/profile_page.html'
    success_msg = None

    def get_form_class(self):
        return EditProfileForm

    def get_context_data(self, **kwargs):
        user_model = self.model.objects.get(username=self.request.user.username)
        kwargs['list_data'] = user_model
        kwargs['purchases'] = Purchases.objects.filter(buyer=user_model)
        return super().get_context_data(**kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user = self.request.user
        if user == kwargs['instance']:
            return kwargs
        return self.handle_no_permission()

    def get_success_url(self, **kwargs):
        return reverse_lazy('profile', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        add_balance = request.POST.get('add_balance_to_user')
        if add_balance and add_balance.isdigit():
            new_balance = request.user.balance + float(add_balance)
            UserProfile.objects.filter(id=request.user.id).update(balance=new_balance)
        return super().post(request, *args, **kwargs)
