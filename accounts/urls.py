from django.urls import re_path as url
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from app.views.index import Landing

from . import views

app_name = "accounts"

urlpatterns = (
    [
        path("portal/", Landing.as_view(), name="home"),
        path("portal/login/", views.Login.as_view(), name="login"),
        path("portal/logout/", views.Logout.as_view(), name="logout"),
        path("portal/profile/", views.Profile.as_view(), name="profile"),
        path("portal/register/", views.Register.as_view(), name="register"),
        path(
            "portal/register/complete/",
            views.RegistrationComplete.as_view(),
            name="django_registration_complete",
        ),
        path(
            "portal/register/closed/",
            views.RegistrationClosed.as_view(),
            name="django_registration_disallowed",
        ),
        path(
            "portal/activation/<str:activation_key>/",
            views.ActivateUser.as_view(),
            name="registration_activate",
        ),
        path(
            "portal/activation/complete/",
            views.ActivationComplete.as_view(),
            name="django_registration_activation_complete",
        ),
        path(
            "portal/change_password/", views.ChangePassword.as_view(), name="change_password"
        ),
        path(
            "portal/change_password_done/",
            views.ChangePasswordDone.as_view(),
            name="change_password_done",
        ),
        path("portal/reset_password/", views.ResetPassword.as_view(), name="reset_password"),
        path(
            "reset_password_sent/",
            views.ResetPasswordDone.as_view(),
            name="password_reset_done",
        ),
        path(
            "portal/reset/<uid64>/<token>",
            views.ResetPasswordConfirm.as_view(),
            name="password_reset_confirm",
        ),
        path(
            "portal/reset_password_complete/",
            views.ResetPasswordComplete.as_view(),
            name="password_reset_complete",
        ),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
