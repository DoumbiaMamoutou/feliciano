# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models


class MainConfigAdmin(admin.ModelAdmin):

    list_display = (
        'afficheImage1',
        'afficheImage2',
        'afficheImage3',
        'affichescrollImage',
        'nom',
        'description',
        'instagram',
        'text1',
        'text2',
        'text3',
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
        'tel',
        'email',
        'status',
        'date_add',
        'date_upd',
    )
    def afficheImage1(self, obj):
        return mark_safe('<img src="{url}" width="100px" heigth="50px" />'.format(url=obj.image1.url))
    def afficheImage2(self, obj):
        return mark_safe('<img src="{url}" width="100px" heigth="50px" />'.format(url=obj.image2.url))
    def afficheImage3(self, obj):
        return mark_safe('<img src="{url}" width="100px" heigth="50px" />'.format(url=obj.image3.url))
    def affichescrollImage(self, obj):
        return mark_safe('<img src="{url}" width="100px" heigth="50px" />'.format(url=obj.scroll_image.url))


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
        'Image1',
        'Image2,
        'Image3',
        'Image4',
        'Image5',
        'Image6',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'status',
        'date_add',
        'date_upd',
    )
    def Image1(self, obj):
        return mark_safe('<img src="{url}" width="100px" heigth="50px" />'.format(url=obj.image1.url))
    
    def Image2(self, obj):
        return mark_safe('<img src="{url}" width="100px" heigth="50px" />'.format(url=obj.image2.url))
    def Image3(self, obj):
        return mark_safe('<img src="{url}" width="100px" heigth="50px" />'.format(url=obj.image3.url))
    def Image4(self, obj):
        return mark_safe('<img src="{url}" width="100px" heigth="50px" />'.format(url=obj.image4.url))
    
    def Image5(self, obj):
        return mark_safe('<img src="{url}" width="100px" heigth="50px" />'.format(url=obj.image5.url))
    
    def Image6(self, obj):
        return mark_safe('<img src="{url}" width="100px" heigth="50px" />'.format(url=obj.image6.url))


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
        'Image',
        'name',
        'job',
        'comment',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'name',
        'job',
        'comment',
        'status',
        'date_add',
        'date_upd',
    )
    def Image(self, obj):
        return mark_safe('<img src="{url}" width="100px" heigth="50px" />'.format(url=obj.image.url))
    search_fields = ('name',)

class ContactConfigAdmin(admin.ModelAdmin):
    list_display = (
        'imageContact',
        'titre',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'titre',
        'status',
        'date_add',
    )
    def imageContact(self, obj):
        return mark_safe('<img src="{url}" width="100px" heigth="50px" />'.format(url=obj.image.url))
    
class BlogConfigAdmin(admin.ModelAdmin):
    list_display = (
        'imageBlog',
        'titre',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'titre',
        'status',
        'date_add',
    )
    def imageBlog(self, obj):
        return mark_safe('<img src="{url}" width="100px" heigth="50px" />'.format(url=obj.image.url))

class MenuConfigAdmin(admin.ModelAdmin):
    list_display = (
        'imageMenu',
        'titre',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'titre',
        'status',
        'date_add',
    )
    def imageMenu(self, obj):
        return mark_safe('<img src="{url}" width="100px" heigth="50px" />'.format(url=obj.image.url))

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
_register(models.ContactConfig, ContactConfigAdmin)
_register(models.BlogConfig, BlogConfigAdmin)
_register(models.MenuConfig, MenuConfigAdmin)