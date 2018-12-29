from django.urls import path
from . import views

app_name = "ToDoList_app"

urlpatterns =[

    # home route
    path('',views.home_view,name="home_page"),
    path('delete/<list_item_id>',views.delete_item,name="delete_list_item"),
    path('crossoff/<list_item_id>',views.crossoff_item,name="crossoff_item"),
    path('uncross/<list_item_id>',views.uncross_item,name="uncross_item"),
    path('edit/<list_item_id>',views.edit_item, name = "edit_item"),

]