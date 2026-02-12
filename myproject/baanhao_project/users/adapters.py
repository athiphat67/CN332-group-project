from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.exceptions import ImmediateHttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import User, UserRole


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    """
    Custom adapter that:
    - Redirects social signup users to fill extra info, then requires admin approval.
    - Blocks signup when user tries to login via provider without an existing account.
    - Handles email conflicts from providers gracefully.
    """

    def is_open_for_signup(self, request, sociallogin):
        """
        If the user came from the LOGIN page (session flag), block signup
        and redirect back with an error message.
        Otherwise allow signup (from register page).
        """
        if request.session.pop('social_action', None) == 'login':
            messages.error(
                request,
                "You don't have an account yet. Please sign up first."
            )
            raise ImmediateHttpResponse(redirect('users:login'))
        return True

    def populate_user(self, request, sociallogin, data):
        """
        Ensure user always has an email so allauth can auto-signup.
        If provider email already exists in DB, use a placeholder instead
        so auto-signup proceeds, then let the extra info form handle it.
        """
        user = super().populate_user(request, sociallogin, data)

        # Check if provider email already exists in DB
        if user.email and User.objects.filter(email=user.email).exists():
            # Clear the conflicting email — user will enter a new one in extra info form
            user.email = f'{sociallogin.account.uid}@placeholder.local'
            # Also clear sociallogin.email_addresses so allauth doesn't check it
            sociallogin.email_addresses = []
        elif not user.email:
            # Provider didn't provide email at all (e.g. LINE without email permission)
            user.email = f'{sociallogin.account.uid}@placeholder.local'

        return user

    def save_user(self, request, sociallogin, form=None):
        """Save user and redirect to extra info form."""
        user = super().save_user(request, sociallogin, form)
        user.is_active = False
        user.role = UserRole.RESIDENT
        user.save()

        # Store user id and provider in session for the extra info view
        request.session['social_signup_user_id'] = user.id
        request.session['social_signup_provider'] = sociallogin.account.provider

        # Redirect to extra info form instead of logging in
        raise ImmediateHttpResponse(redirect('users:social_extra_info'))

    def pre_social_login(self, request, sociallogin):
        """
        Handle returning social login users.
        - Inactive user (pending approval): show message and redirect to register.
        - Active user from register page: redirect to login with message.
        - Active user from login page: let allauth log them in normally.
        """
        user = sociallogin.user
        if not user.pk:
            return  # New user, let the signup flow handle it

        if not user.is_active:
            # User already signed up but is pending admin approval
            messages.info(
                request,
                "You have already signed up with this account. "
                "Your registration is pending admin approval."
            )
            raise ImmediateHttpResponse(redirect('users:register'))

        # Active user — check if they came from login or register page
        if request.session.pop('social_action', None) != 'login':
            # Came from register page but already has an active account
            messages.info(
                request,
                "You already have an account. Please sign in instead."
            )
            raise ImmediateHttpResponse(redirect('users:login'))
        # From login page → let allauth log them in normally
