from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash, get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from account.form import LoginUserForm, CreateUserForm
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin



# Create your views here.
def login_request(request):
    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        form = LoginUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            username = User.objects.get(email=email).username
            user = authenticate(request, username=username, password=password)

            if user is not None:

                if user.is_staff:
                    login(request, user)
                    messages.success(request, "Giriş başarılı!")
                    return redirect("indexadmin")
                else:
                    login(request, user)
                    messages.success(request, "Giriş başarılı!")
                    return redirect("index")

            else:
                messages.error(request, "Email ya da parola yanlış!")
                return render(request, 'account/login.html', {'form': form})
        else:
            messages.error(request, "Formu eksiksiz doldurmalısınız!")
            return render(request, 'account/login.html', {'form': form})

    form = LoginUserForm()
    return render(request, 'account/login.html', {'form': form})

def register_request(request):
    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():

            if form.cleaned_data.get('email')[-10:] != "idu.edu.tr" :
                messages.info(request, "Sadece Okul Mailinizle Kayıt Olabilirsiniz!")
                return render(request, 'account/register.html', {"form": form})

            user = form.save(commit=False)
            user.is_active = False
            user.save()
            messages.info(request, "Aktivasyon linki mailinize gönderildi!")
            # to get the domain of the current site
            current_site = get_current_site(request)
            mail_subject = 'İzmir Demokrasi Üniversitesi Ders Takip Sistemi Aktivasyon Maili'
            message = render_to_string('account/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return redirect('login')
        else:
            form = CreateUserForm()
            return render(request, 'account/register.html', {"form": form})

    form = CreateUserForm()
    return render(request, 'account/register.html', {"form": form})

def activate(request, uidb64, token):
    user = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        messages.info(request, "Hesabınıza giriş yapabilirsiniz!")
        user.save()
        return render(request, 'account/mailmessage.html')
    else:
        return render(request, 'account/mailinvalid.html')

def change_password(request):

    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            logout(request)
            messages.success(request, "Şifre değiştirildi!")
            return redirect("login")
        else:
            messages.error(request, "Şifre değiştirilemedi!")
            return render(request, "account/change_password.html", {"form":form})
    form = PasswordChangeForm(request.user)
    return render(request, "account/change_password.html", {"form":form})

def sifre(request):
    return render(request, 'account/sifre.html')

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'account/password_reset.html'
    email_template_name = 'account/password_reset_email.html'
    subject_template_name = 'account/password_reset_subject'
    success_message = "Parola sıfırlama talebinizi E-Mailinize gönderdik. " \
                      "E-Mail hesabınıza giderek şifrenizi sıfırlayabilirsiniz. " \
                      " Eğer bir E-Mail almadıysanız "  \
                      "Lütfen E-Mail hesabınızı düzgün yazdığınızdan ve Spam klasörünüzü kontrol ettiğinizden emin olun."
    success_url = reverse_lazy('login')

def logout_request(request):
    logout(request)
    messages.success(request, "Çıkış başarılı!")
    return redirect("login")