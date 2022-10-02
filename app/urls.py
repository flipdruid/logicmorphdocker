from django.urls import path

from app.views.index import landing

urlpatterns = [
    path("", landing, name="main"),
]
