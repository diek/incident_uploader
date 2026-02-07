# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.html import format_html
from sorl.thumbnail import get_thumbnail

from .models import IncidentImage, IncidentReport, Location, Shift


# IMPORTANT: Define the inline BEFORE the admin class that uses it
class IncidentImageInline(admin.TabularInline):
    model = IncidentImage
    extra = 1
    can_delete = True
    ordering = ("order", "uploaded_at")

    readonly_fields = ("thumbnail",)
    fields = (
        "thumbnail",
        "image",
        "caption",
        "order",
    )

    def thumbnail(self, obj):
        if not obj.pk or not obj.image:
            return "—"

        try:
            thumb = get_thumbnail(
                obj.image,
                "200x200",
                crop="center",
                quality=85,
            )
            return format_html(
                '<a href="{}" target="_blank">'
                '<img src="{}" style="max-width:200px; height:auto;" />'
                "</a>",
                obj.image.url,
                thumb.url,
            )
        except Exception as e:
            return f"Error: {e}"

    thumbnail.short_description = "Preview"


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("id", "location")


@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ("id", "shift", "employee", "location")
    raw_id_fields = ("employee", "location")


@admin.register(IncidentReport)
class IncidentReportAdmin(admin.ModelAdmin):
    inlines = [IncidentImageInline]

    list_display = (
        "id",
        "shift",
        "date_time_incident",
        "summary",
        "merchandise_cost",
        "is_multiple_person",
        "number_persons",
        "merchandise_description",
        "is_theft",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "shift",
        "date_time_incident",
        "is_multiple_person",
        "is_theft",
    )
    date_hierarchy = "date_time_incident"


@admin.register(IncidentImage)
class IncidentImageAdmin(admin.ModelAdmin):
    readonly_fields = ("thumbnail",)

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "incident_report",
                    "thumbnail",
                    "image",
                    "caption",
                    "order",
                )
            },
        ),
    )
    list_display = (
        "incident_report",
        "thumbnail",
        "caption",
        "uploaded_at",
        "order",
    )

    list_filter = ("incident_report", "uploaded_at")

    def thumbnail(self, obj):
        if not obj.image:
            return "—"

        try:
            thumb = get_thumbnail(
                obj.image,
                "120x120",
                crop="center",
                quality=85,
            )
            return format_html(
                '<a href="{}" target="_blank">'
                '<img src="{}" width="{}" height="{}" style="object-fit: cover;" />'
                "</a>",
                obj.image.url,
                thumb.url,
                thumb.width,
                thumb.height,
            )
        except Exception as e:
            return f"Error: {e}"

    thumbnail.short_description = "Image"
