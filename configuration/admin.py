from django.utils.safestring import mark_safe

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class MainConfigAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',
        'description',
        'instagram',
        'text1',
        'text2',
        'text3',
        'image1',
        'image2',
        'image3',
        'scroll_image',
        'tel',
        'email',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'instagram',
        'status',
        'date_add',
        'date_upd',
        'social',
        'id',
        'nom',
        'description',
        'working_hour',
        'instagram',
        'text1',
        'text2',
        'text3',
        'image1',
        'image2',
        'image3',
        'scroll_image',
        'tel',
        'email',
        'status',
        'date_add',
        'date_upd',
    )


class DayAdmin(admin.ModelAdmin):

    list_display = ('id', 'jour', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'jour',
        'status',
        'date_add',
        'date_upd',
    )


class WorkingHourAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'jour',
        'start_hour',
        'end_hour',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'jour',
        'status',
        'date_add',
        'date_upd',
        'id',
        'jour',
        'start_hour',
        'end_hour',
        'status',
        'date_add',
        'date_upd',
    )


class InstagramAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'image1',
        'image2',
        'image3',
        'image4',
        'image5',
        'image6',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'image1',
        'image2',
        'image3',
        'image4',
        'image5',
        'image6',
        'status',
        'date_add',
        'date_upd',
    )


class SocialAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'lien', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'name',
        'lien',
        'status',
        'date_add',
        'date_upd',
    )
    search_fields = ('name',)


class IconAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'name',
        'status',
        'date_add',
        'date_upd',
    )
    search_fields = ('name',)


class AboutConfigAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'content',
        'open_hour',
        'phone',
        'yoe',
        'menu',
        'satff',
        'happy_customer',
        'description',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'titre',
        'content',
        'open_hour',
        'phone',
        'yoe',
        'menu',
        'satff',
        'happy_customer',
        'description',
        'status',
        'date_add',
        'date_upd',
    )


class ServiceConfigAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'description',
        'icone',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'icone',
        'status',
        'date_add',
        'date_upd',
        'id',
        'titre',
        'description',
        'icone',
        'status',
        'date_add',
        'date_upd',
    )


class TemoinAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'job',
        'comment',
        'image',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'name',
        'job',
        'comment',
        'image',
        'status',
        'date_add',
        'date_upd',
    )
    search_fields = ('name',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.MainConfig, MainConfigAdmin)
_register(models.Day, DayAdmin)
_register(models.WorkingHour, WorkingHourAdmin)
_register(models.Instagram, InstagramAdmin)
_register(models.Social, SocialAdmin)
_register(models.Icon, IconAdmin)
_register(models.AboutConfig, AboutConfigAdmin)
_register(models.ServiceConfig, ServiceConfigAdmin)
_register(models.Temoin, TemoinAdmin)
