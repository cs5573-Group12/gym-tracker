from django.urls import include, path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', login_required(views.members), name='members'),
    path('new/', login_required(views.add_member), name='add_member'),
    # path('members/<int:member_id>/', views.member_detail, name='member_detail'),
    path('<int:member_id>/', login_required(views.edit_member), name='edit_member'),
    path('<int:member_id>/delete/', login_required(views.delete_member), name='delete_member'),
    path('check_in/', login_required(views.member_check_in), name='member_check_in'),
]