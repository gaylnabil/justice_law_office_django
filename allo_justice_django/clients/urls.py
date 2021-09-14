from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('login/', views.client_login, name='client_login'),
    # path('logout/', views.client_logout, name='client_logout'),
    path('register/', views.client_register, name='client_register'),
    path('verification/<str:email>', views.client_verification,
         name='client_verification'),
    path('activate/<uidb64>/<token>/',
         views.client_activate, name='client_activate'),

    # path('login/', auth_views.LoginView.as_view(template_name='clients/login.html'), name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='clients/password_reset.html'), name='client_password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='clients/password_reset_done.html'), name='client_password_reset_done'),
    path('password_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(), name='client_password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='clients/password_reset_complete.html'), name='client_password_reset_complete'),
    path('change_password/', auth_views.PasswordChangeView.as_view(),
         name='client_password_change'),
    path('profile/', views.client_profile, name='client_profile'),

]
