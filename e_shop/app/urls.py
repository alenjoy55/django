from django.urls import path
from . import views


urlpatterns=[
    path('',views.shop_login),
    path('logout',views.shop_logout),
    path('register',views.register),

    #-------admin-------------
    path('shop_home',views.shop_home),
    path('add_product',views.add_product),
    path('edit_product/<id>',views.edit_product),
    path('delete_product/<id>',views.delete_product),

    #------user---------------
    path('user_home',views.user_home),
]