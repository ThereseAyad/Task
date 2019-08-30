from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns= [
    path('login/', auth_views.LoginView.as_view(template_name='Task/login.html'), name='login'),
    path('register/', views.UserFormView.as_view(), name='register'),
    path('home/', views.home, name='home'),
    path('profile/', views.MyProfileView, name='profile'),
    path('upload/', views.simple_upload, name='upload'),
    path('reset/', auth_views.PasswordResetView.as_view( template_name='Task/password_reset_form.html',
                                                         email_template_name='Task/password_reset_email.html',
                                                         subject_template_name='Task/password_reset_subject.txt'),
        name='password_reset'),
    path('reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='Task/password_reset_done.html'),
        name='password_reset_done'),
    path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
        auth_views.PasswordResetConfirmView.as_view(template_name='Task/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='Task/password_reset_complete.html'),
        name='password_reset_complete'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('ajax/validate_username/', views.validate_username, name='validate_username'),
    path('ajax/', views.index, name="index"),
    path('insert/', views.insert, name="insert"),
    path('distance/', views.distance, name='distance'),

]