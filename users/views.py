from django.shortcuts import render
from .forms import UserRegistrationForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views import generic


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})