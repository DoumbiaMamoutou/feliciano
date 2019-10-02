# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models


class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        'imageArticle',
        'titre',
        'description',
        'contenu',
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
        'category',
        'author',
        'status',
        'date_add',
        'date_upd',
    )
    def imageArticle(self, obj):
        return mark_safe('<img src="{url}" width="100px" heigth="50px" />'.format(url=obj.image.url))
    
    raw_id_fields = ('tag',)


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('imageCategory', 'titre', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'titre',
        'status',
        'date_add',
        'date_upd',
    )
    def imageCategory(self, obj):
        return mark_safe('<img src="{url}" width="100px" heigth="50px" />'.format(url=obj.image.url))


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
        'imageComment',
        'article',
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
        'article',
        'message',
        'name',
        'email',
        'website',
        'status',
        'date_add',
        'date_upd',
    )
    def imageComment(self, obj):
        return mark_safe('<img src="{url}" width="100px" heigth="50px" />'.format(url=obj.image.url))
    
    search_fields = ('name',)


class AuthorAdmin(admin.ModelAdmin):

    list_display = ('imageAuthor', 'user', 'description')
    list_filter = ('user', 'id', 'user', 'description')
    def imageAuthor(self, obj):
        return mark_safe('<img src="{url}" width="100px" heigth="50px" />'.format(url=obj.image.url))


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Article, ArticleAdmin)
_register(models.Category, CategoryAdmin)
_register(models.Tag, TagAdmin)
_register(models.Comment, CommentAdmin)
_register(models.Author, AuthorAdmin)
