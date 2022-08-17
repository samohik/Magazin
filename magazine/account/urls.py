from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.AuthenticateView.as_view(), name='login'),
    path('logout/', views.LogOutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.ProfileUser.as_view(), name='profile'),
    path('change_password/', views.ChangePasswordView.as_view(), name='change_password'),
    path('edit_profile/', views.EditProfileView.as_view(), name='edit_profile'),

    path('admin_login/', auth_views.LoginView.as_view(), name='admin_login'),
    path('admin_logout/', auth_views.LogoutView.as_view(), name='admin_logout'),

    # path('profile_test/', views.ProfileExample.as_view()),
    # path('account_test/', views.Account.as_view()),
]
