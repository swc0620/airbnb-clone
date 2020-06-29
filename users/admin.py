from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.

# There are 2 ways of making the model show up on the admin page
# 1. decorator
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    # # list_display controls which fields are displayed on the list page
    # list_display = ("username", "email", "gender", "language", "currency", "superhost")
    # # list_filter adds filter box
    # list_filter = (
    #     "language",
    #     "currency",
    #     "superhost",
    # )

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile", 
            {
                "fields": (
                    "avatar", 
                    "gender", 
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                    "login_method",
                )
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
        "email_verified",
        "email_secret",
        "login_method",
    )


# 2. register
# admin.site.register(models.User, CustomUserAdmin)
