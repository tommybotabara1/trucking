from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('database_operations/', views.database_operations, name='database_operations'),
    path('database_operations/newDBO', views.new_database_operation, name='new_database_operation'),
    path('database_operations/editDBO/<int:id>', views.edit_database_operation, name='edit_database_operation'),
    path('database_operations/deleteDBO/<int:id>', views.delete_database_operation, name='delete_database_operation'),
    path('users/', views.users, name='users'),
    path('testing/', views.testing, name='testing'),
    path('add_new_driver/', views.add_new_driver, name='add_new_driver'),
    path('add_new_customer/', views.add_new_customer, name='add_new_customer'),
    path('add_new_client/', views.add_new_client, name='add_new_client'),
    path('add_new_split_amount/', views.add_new_split_amount, name='add_new_split_amount'),
    path('get_split_amount/', views.get_split_amount, name='get_split_amount'),
    path('get_split_amount_total/', views.get_split_amount_total, name='get_split_amount_total'),
    path('delete_split_amount/', views.delete_split_amount, name='delete_split_amount'),
]
