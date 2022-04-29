from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
def home(request):
    return render(request, 'register/home.html')


def register(request):
    form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'User has been registered.')
    
    return render(request, 'register/register.html', {'form':form})
