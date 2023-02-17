from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth import login, authenticate #add this


# Create your views here.
def register(response):
    if response.method == "POST":
        form = NewUserForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("login")
    else:
        form = NewUserForm()

    return render(response, "register.html", {"form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("book:index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})