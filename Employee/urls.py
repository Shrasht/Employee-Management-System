from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('',views.index,name="index"),
   path('add',views.add,name="add"),
   path('delete/',views.delete,name="delete"),
   path('delete/delete/<int:emp_id>',views.delete,name="delete_id"),
  path('all/',views.all,name="all"),
  path('filter/',views.filter,name="filter"),
]
