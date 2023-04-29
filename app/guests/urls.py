from django.urls import include, path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', login_required(views.guests), name='guests'),
    path('new/', login_required(views.add_guest), name='add_guest'),
    path('<int:guest_id>/', login_required(views.edit_guest), name='edit_guest'),
    path('<int:guest_id>/delete/', login_required(views.delete_guest), name='delete_guest'),
]