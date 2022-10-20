from django.urls import path
from app.views.index import Landing
from app.views import LeadCreate
from app.views import PostCreate
from app.views import PostDelete
from app.views import PostEdit
from app.views import PostView


urlpatterns = [
    path("", Landing.as_view(), name="main"),
    path("contactus/", LeadCreate.as_view(), name="contact_us"),
    path("post/", PostCreate.as_view(), name="post"),
    path("postview/<str:pk>", PostView.as_view(), name="post_view"),
    path("postedit/<str:pk>", PostEdit.as_view(), name="post_edit"),
    path("postdelete/<str:pk>", PostDelete.as_view(), name="post_delete"),
]
