from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('search/',views.search,name="search"),
    path('search1/',views.search1,name="search1"),
]