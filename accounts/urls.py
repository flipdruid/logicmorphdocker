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
        url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
        url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
        path("", Landing.as_view(), name="home"),
        path("logic/login/", views.Login.as_view(), name="login"),
        path("logout/", views.Logout.as_view(), name="logout"),
        path("profile/", views.Profile.as_view(), name="profile"),
        path("lm-link-register/", views.Register.as_view(), name="register"),
        path(
            "register/complete/",
            views.RegistrationComplete.as_view(),
            name="django_registration_complete",
        ),
        path(
            "register/closed/",
            views.RegistrationClosed.as_view(),
            name="django_registration_disallowed",
        ),
        path(
            "activation/<str:activation_key>/",
            views.ActivateUser.as_view(),
            name="registration_activate",
        ),
        path(
            "activation/complete/",
            views.ActivationComplete.as_view(),
            name="django_registration_activation_complete",
        ),
        path(
            "change_password/", views.ChangePassword.as_view(), name="change_password"
        ),
        path(
            "change_password_done/",
            views.ChangePasswordDone.as_view(),
            name="change_password_done",
        ),
        path("reset_password/", views.ResetPassword.as_view(), name="reset_password"),
        path(
            "reset_password_sent/",
            views.ResetPasswordDone.as_view(),
            name="password_reset_done",
        ),
        path(
            "reset/<uid64>/<token>",
            views.ResetPasswordConfirm.as_view(),
            name="password_reset_confirm",
        ),
        path(
            "reset_password_complete/",
            views.ResetPasswordComplete.as_view(),
            name="password_reset_complete",
        ),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
