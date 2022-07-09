from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Profile, User


class UserAdminForm(UserAdmin):
    model = User
    list_display = ('mobile','is_staff', 'is_active',)
    list_filter = ('mobile','name', 'is_staff', 'is_active',)
    fieldsets = (
        ('Requirements', {'fields': ('mobile', 'password' )}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Account Status', {'fields': ('mobile_verified', 'email_is_verified')}),
        ('Personal Information', {'fields': ('name','email')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('mobile', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('mobile',)
    ordering = ('mobile',)


admin.site.register(User, UserAdminForm)
admin.site.register(Profile)
