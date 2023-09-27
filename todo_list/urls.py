from django.urls import path
from todo_list import views

urlpatterns = [
    path('todos/', views.index, name="todos"),
    path('del/<str:item_id>', views.remove, name="del"),
    path('change/<str:item_id>', views.changeStatus, name="change"),
]