from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'

urlpatterns = [
    # Staff list
    path('staff/', views.staff_list, name='staff_list'),
    path('staff/<int:staff_id>/', views.staff_detail, name='staff_detail'),
    
    # Authentication
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('social-extra-info/', views.social_extra_info_view, name='social_extra_info'),
    path('social-login/<str:provider>/', views.social_login_check_view, name='social_login_check'),
    
    # Admin: Registration Approval
    path('pending-registrations/', views.pending_registrations_view, name='pending_registrations'),
    path('approve-registration/<int:request_id>/', views.approve_registration_view, name='approve_registration'),
    path('reject-registration/<int:request_id>/', views.reject_registration_view, name='reject_registration'),
    
    # Password Reset
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='users/password_reset_form.html',
        email_template_name='users/password_reset_email.html',
        success_url='/users/password_reset/done/'
    ), name='password_reset'),
    
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'
    ), name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html',
        success_url='/users/reset/done/'
    ), name='password_reset_confirm'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'
    ), name='password_reset_complete'),
]
