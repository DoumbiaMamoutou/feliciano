from django.urls import path,include
from . import views


urlpatterns = [
	path('blog', views.blog, name= 'blog'),
    path('single/<int:id>', views.single, name= 'single'),
    path('listcat/<str:category>', views.list_categorie, name= 'listcat'),
    path('listdate/<str:date>', views.list_date, name= 'listdate'),
    path('listtag/<str:tag>', views.list_tag, name= 'listtag'),
    path('fake',views.artFake),
    path('comfake',views.comFake),
]