from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.forms import ModelForm
from .models import UserProfile


class AuthUserForm(AuthenticationForm, ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    class Meta:
        model = UserProfile
        fields = ('username', 'password')


class RegisterUserForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'password', 'first_name', 'last_name', 'city', 'date_of_birthday', 'phone_number')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            group, _ = Group.objects.get_or_create(name='regular_users')
            UserProfile.objects.filter(id=user.id).update(groups=group)
        return user


class EditProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'city', 'phone_number', 'date_of_birthday')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control mb-4'
