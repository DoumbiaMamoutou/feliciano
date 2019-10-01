from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'description',
        'contenu',
        'image',
        'category',
        'author',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'category',
        'author',
        'status',
        'date_add',
        'date_upd',
        'id',
        'titre',
        'description',
        'contenu',
        'image',
        'category',
        'author',
        'status',
        'date_add',
        'date_upd',
    )
    raw_id_fields = ('tag',)


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'titre', 'image', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'titre',
        'image',
        'status',
        'date_add',
        'date_upd',
    )


class TagAdmin(admin.ModelAdmin):

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


class CommentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'article',
        'image',
        'message',
        'name',
        'email',
        'website',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'article',
        'status',
        'date_add',
        'date_upd',
        'id',
        'article',
        'image',
        'message',
        'name',
        'email',
        'website',
        'status',
        'date_add',
        'date_upd',
    )
    search_fields = ('name',)


class AuthorAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'image', 'description')
    list_filter = ('user', 'id', 'user', 'image', 'description')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Article, ArticleAdmin)
_register(models.Category, CategoryAdmin)
_register(models.Tag, TagAdmin)
_register(models.Comment, CommentAdmin)
_register(models.Author, AuthorAdmin)
