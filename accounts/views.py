from django.shortcuts import reverse
from django.conf import settings
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordChangeDoneView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordContextMixin
from django.contrib.auth.views import PasswordResetCompleteView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic import TemplateView
from django_registration.backends.activation.views import ActivationView
from django_registration.backends.activation.views import RegistrationView

from accounts.forms import UserForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from accounts.decorators import currentauth_user


class IndexView(TemplateView):
    template_name = "accounts/home.html"

@method_decorator(currentauth_user, name="dispatch")
class Login(LoginView):
    template_name = "accounts/login.html"
    
    def get_success_url(self):    
        return reverse('dashboard')

class Logout(LogoutView):
    template_name = "accounts/logged_out.html"

    def get_success_url(self):    
        return reverse('main')


class Profile(UpdateView):
    pass

@method_decorator(login_required, name="dispatch")
class ChangePassword(PasswordChangeView):
    template_name = "accounts/password_change_form.html"
    success_url = reverse_lazy("accounts:login")

@method_decorator(login_required, name="dispatch")
class ChangePasswordDone(PasswordChangeDoneView):
    template_name = "accounts/password_change_done.html"

@method_decorator(login_required, name="dispatch")
class ResetPassword(PasswordResetView):
    template_name = "accounts/password_reset_form.html"

@method_decorator(login_required, name="dispatch")
class ResetPasswordDone(PasswordResetDoneView):
    template_name = "accounts/password_reset_done.html"

@method_decorator(login_required, name="dispatch")
class ResetPasswordConfirm(PasswordResetConfirmView):
    template_name = "accounts/password_reset_confirm.html"

@method_decorator(login_required, name="dispatch")
class ResetPasswordComplete(PasswordResetCompleteView):
    template_name = "accounts/password_reset_complete.html"

class Register(RegistrationView):
    form_class = UserForm
    template_name = "django_registration/registration_form.html"
    success_url = reverse_lazy("accounts:django_registration_complete")


class ActivateUser(ActivationView):
    pass
    # template_name = "django_registration/activate.html"
    # success_url = reverse_lazy("accounts:django_registration_activation_complete")


class ActivationComplete(TemplateView):
    template_name = "django_registration/activation_complete.html"
    success_url = reverse_lazy("accounts:django_registration_activation_complete")


class RegistrationComplete(TemplateView):
    template_name = "django_registration/registration_complete.html"
    success_url = reverse_lazy("accounts:django_registration_activation_complete")


class RegistrationClosed(TemplateView):
    template_name = "django_registration/registration_closed.html"
