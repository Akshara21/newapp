from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'userpg/register.html', {'form': form})

def login(request):
   username = 'not logged in'

   if request.method == 'POST':
      MyLoginForm = LoginForm(request.POST)

      if MyLoginForm.is_valid():
         username = MyLoginForm.cleaned_data['username']
         request.session['username'] = username
      else:
         MyLoginForm = LoginForm()
   return render(request, 'profile.html', {"username" : username})

def formView(request):
   if request.session.has_key('username'):
      username = request.session['username']
      return render(request, 'profile.html', {"username" : username})
   else:
      return render(request, 'login.html', {})

@login_required
def profile(request):
    return render(request, 'userpg/profile.html')
