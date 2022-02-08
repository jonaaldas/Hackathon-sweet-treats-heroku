# from django.shortcuts import render, HttpResponse
# from django.contrib import messages
# from .models import *
# # import bcrypt
# import re
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

#################### ADDED ##################################
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
################### DEFAULT #################################
from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'sweet_treat_app/index.html')

def sweets(request):
    return render(request,'sweet_treat_app/sweets.html')

def about(request):
    return render(request,'sweet_treat_app/about.html')

def inventory(request):
    return render(request,'sweet_treat_app/inventory.html')



# REGISTER

########### register here #####################################
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            ######################### mail system ####################################
            htmly = get_template('user/Email.html')
            d = { 'username': username }
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            ##################################################################
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form, 'title':'reqister here'})
  
################ login forms###################################################
def Login(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' wecome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form':form, 'title':'log in'})



# EMAIL

def signup(request):
    if request.method=="POST":
        username =request.POST["username"]
        password =request.POST["password"]
        email = request.POST["email"]

        user = User.objects.create_user(
                username = username,
                password = password,
                email = email
             )
        login (request,user)
        subject = 'Welcome to Sweet Treats'
        message = f'Hi {user.username}, thank you for signing up to the Sweet Treats mailing list!'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email, ]
        send_mail( subject, message, email_from, recipient_list )
        return redirect("/dashboard/")
    return render(request, "signup.html")