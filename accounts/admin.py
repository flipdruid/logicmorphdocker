from django.contrib import admin

from accounts.models import User, Profile, Customer

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display    =   ('email', 'username','first_name', 'last_name')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display    =   ('user', 'timestamp')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display    =   ('email', 'first_name', 'last_name', 'id')


