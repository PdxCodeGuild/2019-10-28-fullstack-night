
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth


def signup(request):

    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        email = request.POST["email"]

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect("users:signup")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Taken")
                return redirect("users:signup")
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,last_name=last_name)
                user.save()
                messages.info(request,"User created")
        
        else:
            messages.info(request,"Passwords dont match")
            return redirect("users:signup")
        return redirect("login")
    else:
        return render(request,'signup.html')