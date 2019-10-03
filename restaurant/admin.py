
# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin
from django.utils.safestring import mark_safe
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
        'imagePlat',
        'name',
        'prix',
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
        'prix',
        'category',
        'status',
        'date_add',
        'date_upd',
    )
    def imagePlat(self, obj):
        return mark_safe('<img src="{url}" width="100px" heigth="50px" />'.format(url=obj.image.url))
    
    raw_id_fields = ('ingredient',)


class ChefAdmin(admin.ModelAdmin):

    list_display = (
        'imageChef',
        'first_name',
        'poste',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'poste',
        'status',
        'date_add',
        'date_upd',
        'poste',
        'status',
        'date_add',
        'date_upd',
    )
    def imageChef(self, obj):
        return mark_safe('<img src="{url}" width="100px" heigth="50px" />'.format(url=obj.image.url))
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
