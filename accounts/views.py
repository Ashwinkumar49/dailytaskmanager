from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            messages.success(request, "Welcome to Daily Task Manager, {}".format(username))
            return redirect('/')
        else:
            messages.warning(request, "Invalid Credentials")
            return redirect('login.html')
        
    else:
        return render(request, 'login.html')
    
def register(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        #phone = request.POST['phone']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.warning(request, "Username already taken")
                return redirect('register.html')
            elif User.objects.filter(email=email).exists():
                messages.warning(request, "Email already taken")
                return redirect('register.html')
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save();
                messages.success(request, "Registration Successful")
                return redirect('login.html')
        else:
            messages.error(request, "Passwords didn't match")
            return redirect('register.html')
    else:
        return render(request, 'register.html')