
from django.contrib import admin
from app.models import Post, Lead

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'created_by', 'created_at', 'updated_at']

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'entity_name', 'details', 'created_at', 'updated_at']
