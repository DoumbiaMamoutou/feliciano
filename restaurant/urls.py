from django.urls import path, include
from .import views
urlpatterns = [
    path('', views.home, name= 'home'),
    path('about', views.about, name= 'about'),
    path('menu', views.menu, name= 'menu'),
    path('listcat', views.list_categorie, name= 'listcat'),
    path('listdate', views.list_date, name= 'listdate'),
    path('listtag', views.list_tag, name= 'listtag'),
]

