from django.urls import path
from . import views

urlpatterns = [
    path('',views.fakeIcone),
    path('fakeingre',views.fakeIngredient),
    path('fakeplat',views.fakePlat),
    path('temoin',views.fakeTemoin),
]
