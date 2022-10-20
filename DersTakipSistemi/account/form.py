from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import widgets
import random


class LoginUserForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control form-control-user", "placeholder": "Email Giriniz"}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={"class": "form-control form-control-user", "placeholder": "Şifre Giriniz"}))

    def clean_email(self):
        email = self.cleaned_data.get("email")


        if not User.objects.filter(email=email).exists():
            self.add_error("email", "Bu Email ile kayıtlı bir kullanıcı yok!")

        return email


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget = widgets.PasswordInput(attrs={"class": "form-control form-control-user", })
        self.fields["password2"].widget = widgets.PasswordInput(attrs={"class": "form-control form-control-user", })
        self.fields["first_name"].widget = widgets.TextInput(attrs={"class": "form-control form-control-user", })
        self.fields["last_name"].widget = widgets.TextInput(attrs={"class": "form-control form-control-user", })
        self.fields["email"].widget = widgets.TextInput(attrs={"class": "form-control form-control-user", })
        self.fields["email"].required = True
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            self.add_error("email", "Bu Email daha önce kullanılmış!")

        return email

    def confirm_register_allowed(self, user):
        if user.email.startswith('@idu.edu.tr'):
            raise forms.ValidationError("Bu kullanıcı maili ile kayıt olamazsınız!")


    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data.get("password1"))
        user.username = "{}_{}_{}".format(
            self.cleaned_data.get("first_name").replace("ı", "i").replace("ö", "o").lower(),
            self.cleaned_data.get("last_name").lower(),
            random.randint(11111, 99999)
        )

        if commit:
            user.save()

        return user