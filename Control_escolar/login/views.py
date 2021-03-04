from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, "login/login.html")

def password_reset(request):
    return render(request, "login/password_reset.html")

