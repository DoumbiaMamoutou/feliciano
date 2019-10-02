from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class ClientAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'ip',
        'pays',
        'ville',
        'continent',
        'longitude',
        'latitude',
        'reseau',
    )
    list_filter = (
        'id',
        'ip',
        'pays',
        'ville',
        'continent',
        'longitude',
        'latitude',
        'reseau',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Client, ClientAdmin)
