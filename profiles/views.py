from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if request.user.is_authenticated():
        return render(request, 'profiles/index.html', {'user': request.user})
    else:  
        return redirect('account:signin')
