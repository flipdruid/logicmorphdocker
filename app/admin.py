from django.contrib import admin

from app.models.client import Client
from app.models.developer import Developer
from app.models.lead import Lead
from app.models.post import Post
from app.models.project import Project
from app.models.profile import Profile
from app.models.reglink import Reglink
from app.models.AppSettings import Appsetting


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "description",
        "created_by",
        "created_at",
        "updated_at",
    ]


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "state",
        "first_name",
        "last_name",
        "email",
        "entity_name",
        "details",
        "created_at",
        "updated_at",
    ]

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id",  "user", "avatar", "is_logicmorph_staff", "is_dark_theme"]

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "profile",
        "business_name",
        "business_logo",
        "address",
        "telephone_no",
        "position",
    ]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "state", "client", "created_at", "updated_at"]


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ["id",  "role", "state"]


@admin.register(Reglink)
class ReglinkAdmin(admin.ModelAdmin):
    list_display = ["id",  "lead_firstname", "lead_lastname", "lead_mail", "lead_id", "lead_reglink", "link_used", "created_at"]

@admin.register(Appsetting)
class AppsettingAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "is_dark_theme"]

