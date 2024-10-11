from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import transaction
from myapp.models import LogEntry
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User

def create_user(request):
    try:
        user = User.objects.create(username='testuser')
        return HttpResponse("User created!")
    except Exception as e:
        return HttpResponse(f"Error occurred: {e}")

@receiver(post_save, sender=User)

def user_saved_handler(sender, instance, **kwargs):
    print("Signal handler started")

    # Simulate saving a log entry (or any other model)
    log_entry = LogEntry.objects.create(user=instance, message="User created")

    # Simulate an error in the signal handler
    raise Exception("Something went wrong in the signal handler!")

    print("Signal handler finished")
