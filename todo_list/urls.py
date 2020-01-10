from todo_list import views
from django.urls import path

urlpatterns = [
    path('',views.home,name="home"),
	path('delete/<id>',views.delete,name="delete"),
	path('cross_off/<id>',views.cross_off,name="cross_off"),
	path('uncross/<id>',views.uncross,name="uncross"),
	path('edit/<id>',views.edit,name="edit"),
]