from django.shortcuts import render, redirect
from user.forms import UserRegistrationForm

def home(request):
  return render(request, 'home.html')

def register(request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')
  else:
    form = UserRegistrationForm()
  
  context = {
    'form': form
  }

  return render(request, 'register.html', context)

def home(request):
  return render(request, 'home.html')