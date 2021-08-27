from django.contrib import admin

from .models import *


@admin.register(DoctorInfo)
class DoctorInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(SiteUtilitie)
class SiteUtilsAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(AboutText)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['heading']

@admin.register(Subscriber)
class SubsAdmin(admin.ModelAdmin):
    list_display = ['id', 'email']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'heading', 'published_date']

@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'treatment_type']
