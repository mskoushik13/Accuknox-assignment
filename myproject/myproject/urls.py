from django.urls import path, include
from django.http import HttpResponse

# A simple view for the root path
def home(request):
    return HttpResponse("Welcome to the home page!")

urlpatterns = [
    path('', home),  # This is the root path that will match http://127.0.0.1:8000/
    path('myapp/', include('myapp.urls')),  # This will match http://127.0.0.1:8000/myapp/
]
