# from django.shortcuts import render
import email
from http.client import HTTPResponse
from django.views.generic import CreateView
from django.views.generic.edit import FormView

# from django.shortcuts import resolve_url
from .forms import UserForm
from .models import Customer

from django.contrib.auth.views import ( 
LoginView,
LogoutView,
PasswordChangeView,
PasswordChangeDoneView,
PasswordResetView,
PasswordResetDoneView,
PasswordResetConfirmView,
PasswordResetCompleteView,
PasswordContextMixin,

)

from django_registration.backends.activation.views import  RegistrationView, ActivationView
from django.views.generic import TemplateView
from django.urls import reverse_lazy




class ContactUs(CreateView):
    model           =   Customer
    template_name   =   'accounts/contact_us.html' 
    fields          =   '__all__'
    success_url     =   reverse_lazy("accounts:home")    

class IndexView(TemplateView):
    template_name   =   'accounts/home.html'


class Login(LoginView):
    template_name = 'accounts/login.html'

class Logout(LogoutView):
    template_name = 'accounts/logged_out.html'

class Profile(TemplateView):
    model = UserForm
    template_name= 'accounts/account_profile.html'
    context_object_name = 'account'
    

class ChangePassword(PasswordChangeView):
    template_name   =   'accounts/password_change_form.html'
    success_url     =   reverse_lazy("login")

class ChangePasswordDone(PasswordChangeDoneView):
    template_name   =   'accounts/password_change_done.html'
    

class ResetPassword(PasswordResetView):
    template_name   =  'accounts/password_reset_form.html'


class ResetPasswordDone(PasswordResetDoneView):
    template_name   =  'accounts/password_reset_done.html'

class ResetPasswordConfirm(PasswordResetConfirmView):
    template_name   =  'accounts/password_reset_confirm.html'

class ResetPasswordComplete(PasswordResetCompleteView):
    template_name   =  'accounts/passwprd_reset_complete.html'

class Register(RegistrationView):
    form_class = UserForm
    template_name = 'django_registration/registration_form.html'
    success_url = reverse_lazy("accounts:django_registration_complete")

class ActivateUser(ActivationView):    
    template_name = 'django_registration/activate.html'

class ActivationComplete (TemplateView):
    template_name = "django_registration/activation_complete.html"

class RegistrationComplete(TemplateView):
    template_name = "django_registration/registration_complete.html"

class RegistrationClosed(TemplateView):
    template_name = "django_registration/registration_closed.html"




