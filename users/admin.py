from django.contrib import admin
from tabbed_admin import TabbedModelAdmin

from .models import CustomUser
from users.models import FeedbackRequest


@admin.register(CustomUser)
class CustomUserAdmin(TabbedModelAdmin):
    model = CustomUser

    main_tab = (
        ('Main', {
            'fields': (
                'username',
                'password',
                'age',
            )
        }),
    )
    personal_info_tab = (
        ('Personal info', {
            'fields': (
                'email',
                'first_name',
                'last_name',
            )
        }),
    )
    permission_tab = (
        ('Permission', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
            )
        }),
    )
    important_dates_tab = (
        ('Important dates', {
            'fields': (
                'last_login',
                'date_joined',
            )
        }),
    )

    tabs = [
        ('Main', main_tab),
        ('Personal info', personal_info_tab),
        ('Permission', permission_tab),
        ('Important dates', important_dates_tab),
    ]


@admin.register(FeedbackRequest)
class FRAdmin(TabbedModelAdmin):
    model = FeedbackRequest
    main_tab = (
        ('Main', {
            'fields': (
                'name',
                'email',
                'subject',
                'message',
            )
        })
    ),
    status_tab = (
        ('Status', {
            "fields": (
                'status',
            )
        })
    ),

    tabs = [
        ('Main', main_tab),
        ('Status', status_tab),
    ]
