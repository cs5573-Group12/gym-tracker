from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('members/', views.members, name='members'),
    path('members/new/', views.add_member, name='add_member'),
    # path('members/<int:member_id>/', views.member_detail, name='member_detail'),
    path('members/<int:member_id>/', views.edit_member, name='edit_member'),
    path('members/<int:member_id>/delete/', views.delete_member, name='delete_member'),
    path('members/check_in/', views.member_check_in, name='member_check_in'),

    path('employees/', views.employees, name='employees'),
    path('employees/<int:employee_id>/', views.edit_employee, name='edit_employee'),
    path('employees/new/', views.add_employee, name='add_employee'),
    path('employees/<int:employee_id>/delete/', views.delete_employee, name='delete_employee'),

    path('guests/', views.guests, name='guests'),
    path('guests/<int:guest_id>/', views.edit_guest, name='edit_guest'),
    path('guests/new/', views.add_guest, name='add_guest'),
    path('guests/<int:guest_id>/delete/', views.delete_guest, name='delete_guest'),

    path('transactions/', views.transactions, name='transactions'),
    path('settings/', views.settings, name='settings'),
]