import threading
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User

def create_user(request):
    print(f"User creation view is running in thread: {threading.current_thread().name}, ID: {threading.get_ident()}")
    user = User.objects.create(username='testuser')
    return HttpResponse("User created!")
