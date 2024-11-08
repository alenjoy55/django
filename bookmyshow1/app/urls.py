from django.urls import path
from . import views

urlpatterns=[
    path('',views.index_page),
    path('view/<id>',views.view_movie),

]