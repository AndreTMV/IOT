from django.contrib import admin
from .models import Sensor, Reading


class ReadingInline(admin.TabularInline):
    model = Reading
    extra = 0
    readonly_fields = ("value", "readed_at")
    ordering = ("-readed_at",)


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "tipo")
    list_filter = ("tipo",)
    search_fields = ("name",)
    inlines = [ReadingInline]


@admin.register(Reading)
class ReadingAdmin(admin.ModelAdmin):
    list_display = ("id", "sensor", "value", "readed_at")
    list_filter = ("sensor", "readed_at")
    search_fields = ("sensor__name",)
    ordering = ("-readed_at",)
    readonly_fields = ("readed_at",)
