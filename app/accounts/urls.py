from django.urls import include, path
from django.contrib.auth.decorators import login_required
from . import views
from .views import ChangePasswordView

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', login_required(views.logout), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', login_required(views.profile), name='profile'),
    # path('profile/edit/', login_required(views.edit_profile), name='edit_profile'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
]