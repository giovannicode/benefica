from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from customusers.models import UserCreatorForm 
# Create your views here.

def signup(request):
    if request.user.is_authenticated():
        return redirect('profiles:index')
    else:
	if request.method == 'GET':
	    form = UserCreatorForm
	    return render(request, 'account/signup.html', {'form': form})

	elif request.method == 'POST':
	    form = UserCreatorForm(request.POST)

	    if form.is_valid():
		user = form.save()
		user = authenticate(username=form.cleaned_data.get('email'),
				    password=form.cleaned_data.get('password2'))
		login(request, user)
		return redirect('profiles:index')
	    else:
		return render(request, 'account/signup.html', {'form': form})


def signin(request):
    if request.user.is_authenticated():
        return redirect('profiles:index')
    else:
	if request.method == 'GET':
	   form = AuthenticationForm()
	   return render(request, 'account/signin.html', {'form': form})
	   
	elif request.method == 'POST':
	    form = AuthenticationForm(data=request.POST)
	    if form.is_valid():
		login(request, form.get_user())
		return redirect('profiles:index')
	    else:
		return render(request, 'account/signin.html', {'form':form})

def signout(request):
    logout(request)
    return redirect('main:index')
