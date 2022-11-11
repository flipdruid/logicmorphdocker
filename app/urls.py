
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
# from django.contrib.admin.views.decorators import staff_member_required
from app.views.index import Landing
from app.views.lead import LeadCreate, LeadMailList, LeadToClient, LeadMailView, LeadMailDelete, LeadMailViewLead, createreglink, leadactivation, userprofile
from app.views.post import PostCreate, PostDelete, PostEdit, PostView
from app.views.project import CreateProjectClient, CreateProject, ListProject, ListClientProject, ClientProjectUpdate, ClientProjectDelete



urlpatterns = [
    path("", Landing.as_view(), name="main"),
    path("portal/contactus/", LeadCreate.as_view(), name="contact_us"),
    path("portal/leads/", LeadMailList.as_view(), name="lead_mail_lists"),
    # path("leads/", staff_member_required(LeadMailList.as_view()), name="lead_mail_lists"),
    path("portal/mailview/<str:pk>", LeadMailView.as_view(), name="lead_mail_view"),
    path("portal/mailviewlead/<str:pk>", LeadMailViewLead.as_view(), name="lead_mail_view_lead"),
    path("portal/leadclient/<str:pk>", LeadToClient.as_view(), name="lead_client"),
    path("portal/maildelete/<str:pk>", LeadMailDelete.as_view(), name="lead_mail_delete"),
    path("portal/post/", PostCreate.as_view(), name="post"),
    path("portal/postview/<str:pk>", PostView.as_view(), name="post_view"),
    path("portal/postedit/<str:pk>", PostEdit.as_view(), name="post_edit"),
    path("portal/postdelete/<str:pk>", PostDelete.as_view(), name="post_delete"),
    path("portal/createreglink/<str:lead_id>", createreglink, name="create_reg_link"),
    path("portal/leadactivation/<str:reglink>", leadactivation, name="lead_activation_to_client"),
    path("portal/userprofile/", userprofile, name="user_profile"),
    path("portal/createclientproject/", CreateProjectClient.as_view(), name="create_client_project"),
    path("portal/createproject/", CreateProject.as_view(), name="create_project"),
    path("portal/projects/", ListProject.as_view(), name="list_project"),
    path("portal/clientproject/", ListClientProject.as_view(), name="list_client_project"),
    path("portal/clientprojectupdate/<str:pk>", ClientProjectUpdate.as_view(), name="update_client_project"),
    path("portal/clientprojectdelete/<str:pk>", ClientProjectDelete.as_view(), name="delete_client_project"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
