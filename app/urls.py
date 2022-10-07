from django.urls import path

from app.views.index import landing, test


urlpatterns = [
    path("", landing, name="main"),
    path("test", test, name="test"),
]
