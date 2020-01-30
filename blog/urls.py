from django.urls import path,include
from . import views


urlpatterns = [
	path('blog', views.blog, name= 'blog'),
    path('single/<int:id>', views.single, name= 'single'),
    path('comment/<int:id>',views.comment,name='commentaire'),
    path('search',views.blogSearch,name='blog_search'),
    path('listcat/<int:category>', views.list_categorie, name= 'listcat'),
    path('listdate/<str:date>', views.list_date, name= 'listdate'),
    path('listtag/<int:tag>', views.list_tag, name= 'listtag'),
]