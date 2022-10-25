from django.urls import path
from app.views.index import Landing
from app.views.lead import LeadCreate, LeadList
from app.views.post import PostCreate, PostDelete, PostEdit, PostView



urlpatterns = [
    path("", Landing.as_view(), name="main"),
    path("contactus/", LeadCreate.as_view(), name="contact_us"),
    path("leads/", LeadList.as_view(), name="lead_list"),
    path("post/", PostCreate.as_view(), name="post"),
    path("postview/<str:pk>", PostView.as_view(), name="post_view"),
    path("postedit/<str:pk>", PostEdit.as_view(), name="post_edit"),
    path("postdelete/<str:pk>", PostDelete.as_view(), name="post_delete"),
]
