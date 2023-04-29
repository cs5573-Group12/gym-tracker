from django.urls import include, path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', login_required(views.index), name='index'),
    path('members/', include('members.urls')),
    path('guests/', include('guests.urls')),

    path('employees/', login_required(views.employees), name='employees'),
    path('employees/<int:employee_id>/', login_required(views.edit_employee), name='edit_employee'),
    path('employees/new/', login_required(views.add_employee), name='add_employee'),
    path('employees/<int:employee_id>/delete/', login_required(views.delete_employee), name='delete_employee'),

    path('transactions/', login_required(views.transactions), name='transactions'),
    path('settings/', login_required(views.settings), name='settings'),
    path('contact/', login_required(views.contact), name='contact'),
    path('about/', login_required(views.about), name='about'),
]