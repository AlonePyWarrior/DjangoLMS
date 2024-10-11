import codecs
import csv
from datetime import datetime

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.sites.admin import SiteAdmin as DefaultAdminSite
from django.contrib.sites.models import Site
from django.http import HttpResponse

from core.custom_utils import phone_check
from core.forms import CustomUserCreationForm, CustomUserChangeForm
from core.models import CustomUser
from core.templatetags.custom_translation_tags import translate_number
from core.templatetags.persian_calendar_convertor import (
    convert_to_persian_calendar,
    format_persian_datetime,
    persian_date_only
)

admin.site.unregister(Site)


@admin.register(Site)
class SiteAdmin(DefaultAdminSite):
    list_display = ("id", "domain", "name")
    search_fields = ("domain", "name")


def export_users_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = fr'attachment; filename="user_data_{datetime.today().strftime(r"%Y_%m_%d")}.csv"'

    response.write(codecs.BOM_UTF8)

    writer = csv.writer(response)
    writer.writerow(['ID', 'First Name', 'Last Name', 'Province',
                     'Birthdate', 'National ID', 'Phone', 'Email', 'Is Staff'])

    writer.writerows(
        (
            [
                user.id,
                user.first_name,
                user.last_name,
                user.province,
                user.birthdate,
                user.national_id,
                user.phone,
                user.email,
                user.is_staff
            ]
            for user in queryset.iterator()
        )
    )
    response.flush()

    return response


# Add the export function as an admin action
export_users_to_csv.short_description = "دریافت فایل CSV از کاربران انتخاب شده"


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    @admin.display(description='موبایل 📱')
    def phone_(self, obj):
        return translate_number(phone_check(obj.phone))

    @admin.display(description='تاریخ تولد 🎂')
    def birthdate_(self, obj):
        persian_datetime_birthdate = translate_number(
            format_persian_datetime(convert_to_persian_calendar(obj.birthdate)))
        return persian_date_only(persian_datetime_birthdate)

    actions = [export_users_to_csv]

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    'national_id',
                    "phone",
                    "password1",
                    "password2",
                    "email",
                    "country",
                    "province",
                    "city",
                    "birthdate",
                    "gender",
                    "profile_img",
                ),
            },
        ),
    )

    fieldsets = (
        (
            None,
            {
                "fields": (
                    'email',
                    "phone",
                    "gender",
                    "country",
                    "province",
                    "city",
                    "birthdate",
                    "profile_img",
                ),
            },
        ),
        ("اطلاعات هویتی", {
            "fields": ("first_name", "last_name", 'national_id',)}),
        ("رمز عبور", {"fields": ("password",)}),
        (
            "مجوز ها",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("تاریخ های مهم", {"fields": ("last_login", "date_joined")}),
    )

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'id',
        'first_name',
        'last_name',
        'gender',
        'province',
        'birthdate_',
        'national_id',
        'phone_',
        'email',
        'is_staff',
    ]

    list_editable = [
        'is_staff',
    ]
    list_per_page = 20
    search_fields = [
        'first_name__istartswith',
        'last_name__istartswith',
        'national_id',
        'email',
    ]
    list_display_links = [
        'id',
        'national_id',
        'first_name',
        'last_name',
    ]

    ordering = [
        'id',
    ]

    list_filter = (
        'gender',
    )
