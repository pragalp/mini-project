from django.shortcuts import render
from .forms import RegistrationForm

def register(request):
    message = ""
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            message = "Registration Successful!"
            form = RegistrationForm()  # clear form
    else:
        form = RegistrationForm()
    return render(request, "register.html", {"form": form, "message": message})

