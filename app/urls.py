from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from app.views.index import Landing, Dashboard
from app.views.lead import LeadCreate, LeadMailList, LeadToClient, LeadMailView, LeadMailDelete, LeadMailViewLead, createreglink, leadactivation, userprofile, userprofileadminupdate, currentusers, usergroupchange
from app.views.post import PostCreate, PostDelete, PostUpdate, PostView
from app.views.project import CreateProjectClient, CreateProject, ListProject, ListClientProject, ClientProjectUpdate, ClientProjectDelete


urlpatterns = [
    path("", Landing.as_view(), name="main"),
    path("contactus/", LeadCreate.as_view(), name="contact_us"),
    path("leads/", LeadMailList.as_view(), name="lead_mail_lists"),
    path("mailview/<str:pk>/", LeadMailView.as_view(), name="lead_mail_view"),
    path("mailviewlead/<str:pk>/", LeadMailViewLead.as_view(), name="lead_mail_view_lead"),
    path("leadclient/<str:pk>/", LeadToClient.as_view(), name="lead_client"),
    path("maildelete/<str:pk>/", LeadMailDelete.as_view(), name="lead_mail_delete"),
    path("post/", PostCreate.as_view(), name="post"),
    path("postview/<str:pk>/", PostView.as_view(), name="post_view"),
    path("postedit/<str:pk>/", PostUpdate.as_view(), name="post_update"),
    path("postdelete/<str:pk>/", PostDelete.as_view(), name="post_delete"),
    path("createreglink/<str:lead_id>/", createreglink, name="create_reg_link"),
    path("leadactivation/<str:reglink>/", leadactivation, name="lead_activation_to_client"),
    path("userprofile/", userprofile, name="user_profile"),
    path("userprofileview/<str:pk>/", userprofileadminupdate, name="user_profile_adminupdate"),
    path("createclientproject/", CreateProjectClient.as_view(), name="create_client_project"),
    path("createproject/", CreateProject.as_view(), name="create_project"),
    path("projects/", ListProject.as_view(), name="list_project"),
    path("clientprojects/", ListClientProject.as_view(), name="list_client_project"),
    path("clientprojectupdate/<str:pk>/", ClientProjectUpdate.as_view(), name="update_client_project"),
    path("clientprojectdelete/<str:pk>/", ClientProjectDelete.as_view(), name="delete_client_project"),
    path("dashboard/", Dashboard.as_view(), name="dashboard"),
    path("currentusers/", currentusers, name="current_users"),
    path("usergroupchange/", usergroupchange, name="user_group_change"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
