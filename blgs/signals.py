from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver


@receiver(user_logged_in, sender=User)
def login_success(request, sender, user, **kwargs):
    print('---Login signal initialized---')
    print("sender:", sender)
    print("request:", request)
    print("user:", user)
    print("password:", user.password)
    print(f"**Kwargs: {kwargs}")
    print('--- Everything done as Expected ---')

    # Only store relevant, serializable data
    request.session['login_data'] = {
        'sender': str(sender),  # This will store the string representation of the sender
        'user': user.username,
        'password': str(user.password),
        'request': str(request),
        'kwargs': {key: str(value) for key, value in kwargs.items()},  # Ensure all kwargs are serialized
    }


@receiver(user_logged_out, sender=User)
def logout_success(request, sender, user, **kwargs):
    print('---Login signal initialized---')
    print("sender:", sender)
    print("request:", request)
    print("user:", user)
    print("password:", user.password)
    print(f"**Kwargs: {kwargs}")
    print('--- Everything done as Expected ---')

    # Only store relevant, serializable data
    request.session['login_data'] = {
        'sender': str(sender),  # This will store the string representation of the sender
        'user': user.username,
        'password': str(user.password),
        'request': str(request),
        'kwargs': {key: str(value) for key, value in kwargs.items()},  # Ensure all kwargs are serialized
    }
