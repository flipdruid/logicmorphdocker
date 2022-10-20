from django.contrib import admin

from app.models import Client
from app.models import Developer
from app.models import Lead
from app.models import Post
from app.models import Project


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


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = [
        "id",
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
