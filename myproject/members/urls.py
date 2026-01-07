from django.urls import path
from . import views

urlpatterns=[
    path('main',views.main,name='main'),
    path('members/',views.Members,name='members'),
    path('members/details/<int:id>',views.details,name='details'),
    
]