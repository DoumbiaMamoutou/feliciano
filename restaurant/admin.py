from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'titre', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'titre',
        'status',
        'date_add',
        'date_upd',
    )


class PlatAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'prix',
        'image',
        'category',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'category',
        'status',
        'date_add',
        'date_upd',
        'id',
        'prix',
        'image',
        'category',
        'status',
        'date_add',
        'date_upd',
    )
    raw_id_fields = ('ingredient',)


class ChefAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'image',
        'poste',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'user',
        'poste',
        'status',
        'date_add',
        'date_upd',
        'id',
        'user',
        'image',
        'poste',
        'status',
        'date_add',
        'date_upd',
    )
    raw_id_fields = ('social',)


class ReservationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'email',
        'phone',
        'date',
        'person',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'date',
        'status',
        'date_add',
        'date_upd',
        'id',
        'name',
        'email',
        'phone',
        'date',
        'person',
        'status',
        'date_add',
        'date_upd',
    )
    search_fields = ('name',)


class PosteAdmin(admin.ModelAdmin):

    list_display = ('id', 'titre', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'titre',
        'status',
        'date_add',
        'date_upd',
    )


class IngredientAdmin(admin.ModelAdmin):

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


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Category, CategoryAdmin)
_register(models.Plat, PlatAdmin)
_register(models.Chef, ChefAdmin)
_register(models.Reservation, ReservationAdmin)
_register(models.Poste, PosteAdmin)
_register(models.Ingredient, IngredientAdmin)
