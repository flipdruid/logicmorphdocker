from django.urls import path
from app.views.index import Landing
from app.views.lead import LeadCreate, LeadMailList, LeadToClient, LeadMailView, LeadMailDelete, LeadMailViewLead, createreglink, leadactivation
from app.views.post import PostCreate, PostDelete, PostEdit, PostView



urlpatterns = [
    path("", Landing.as_view(), name="main"),
    path("contactus/", LeadCreate.as_view(), name="contact_us"),
    path("leads/", LeadMailList.as_view(), name="lead_mail_lists"),
    path("mailview/<str:pk>", LeadMailView.as_view(), name="lead_mail_view"),
    path("mailviewlead/<str:pk>", LeadMailViewLead.as_view(), name="lead_mail_view_lead"),
    path("leadclient/<str:pk>", LeadToClient.as_view(), name="lead_client"),
    path("maildelete/<str:pk>", LeadMailDelete.as_view(), name="lead_mail_delete"),
    path("post/", PostCreate.as_view(), name="post"),
    path("postview/<str:pk>", PostView.as_view(), name="post_view"),
    path("postedit/<str:pk>", PostEdit.as_view(), name="post_edit"),
    path("postdelete/<str:pk>", PostDelete.as_view(), name="post_delete"),
    path("createreglink/<str:lead_id>", createreglink, name="create_reg_link"),
    path("leadactivation/<str:reglink>", leadactivation, name="lead_activation_to_client"),
]
