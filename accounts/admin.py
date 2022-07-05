from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Profile, User


class UserAdminForm(UserAdmin):
    model = User
    list_display = ('phone_number','is_staff', 'is_active',)
    list_filter = ('phone_number','name', 'is_staff', 'is_active',)
    fieldsets = (
        ('Requirements', {'fields': ('phone_number', 'password' )}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Account Status', {'fields': ('mobile_is_verified', 'email_is_verified')}),
        ('Personal Information', {'fields': ('name','email')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('phone_number',)
    ordering = ('phone_number',)


admin.site.register(User, UserAdminForm)
admin.site.register(Profile)
