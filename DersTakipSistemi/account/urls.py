from django.urls import path, include
from account.views import ResetPasswordView
from . import views
from .views import activate
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', views.login_request, name="login"),
    path('register', views.register_request, name="register"),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', activate,
         name='activate'),
    path('change_password', views.change_password, name="change_password"),
    path('sifre', views.sifre, name="sifre"),
    path('logout', views.logout_request, name="logout"),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
         name='password_reset_complete'),
]