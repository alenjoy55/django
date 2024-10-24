from django.urls import path
from . import views 


urlpatterns=[
    path('display',views.disp),
    path('add_std',views.add_std),
    path('edit_std/<id>',views.edit_std)
    
]