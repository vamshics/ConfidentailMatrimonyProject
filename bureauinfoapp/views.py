from django.shortcuts import render, redirect
from .models import Create_Profile, Age, Stateadd
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout as auth_logout,login as auth_login
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def index(request):
    vamcs = Age.objects.all()
    vam1 = Stateadd.objects.all()
    return render(request,'index.html',{'sa':vamcs,'sst':vam1})
    return render(request, 'index.html')

@login_required
def profile(request):
    imgdata = Create_Profile.objects.all()
    gen=request.POST.get('gender')
    age=request.POST.get('agee')
    stat=request.POST.get('state11')
    city=request.POST.get('cityname1')
    if gen:
        imgdata=imgdata.filter(gender=gen)
    if age:
        imgdata=imgdata.filter(age=age)
    if stat:
        imgdata=imgdata.filter(state=stat)
    if city:
        imgdata=imgdata.filter(city=city)

    return render(request, 'profiles.html',{'akshay':imgdata})
def step(request):
    xyz = Age.objects.all()
    rvk = Stateadd.objects.all()
    return render(request, 'step1.html',{'vamshi':xyz,'addstate':rvk})
def viewprofile(request,id):
    rv = Create_Profile.objects.get(id=id)
    return render(request, 'viewprofile.html',{'kcr':rv})
def save(request):
    updatedata = request.POST.get('rrvk')
    firstname1 = request.POST.get('fname')
    lasttname1 = request.POST.get('sname')
    email1 = request.POST.get('email')
    phonenumber = request.POST.get('phno')
    sgender = request.POST.get('gender1')
    sage = request.POST.get('age1')
    shobbies = request.POST.get('hobbies1')
    abc = Age.objects.get(id=sage)
    statename1 = request.POST.get('statename')
    rvk1 = Stateadd.objects.get(id=statename1)
    cityname = request.POST.get('cityname1')
    sabout = request.POST.get('about1')
    upload1 = request.FILES.get('myfiles[]')
    if updatedata == '':
        ss = Create_Profile(firstname=firstname1, lastname=lasttname1, email=email1,
                        phoneno=phonenumber, gender = sgender,age=abc,hobbies=shobbies, state=rvk1, city=cityname,
                        about=sabout,upload=upload1)
        ss.save()
        return render(request, 'step1.html')
    else:
        rvkr= Create_Profile.objects.filter(id=updatedata).update(firstname=firstname1, lastname=lasttname1, email=email1,
                        phoneno=phonenumber, gender = sgender,age=abc,hobbies=shobbies, state=rvk1, city=cityname,
                        about=sabout,upload=upload1)
        return render(request,'step1.html',{'ss':rvkr})
def edit(request,id):
    bb = Create_Profile.objects.get(id=id)
    xyz = Age.objects.all()
    rvk = Stateadd.objects.all()
    return render(request, 'step1.html', {'ss': bb,'vamshi':xyz,'addstate':rvk})
def delete(request, id):
   person = Create_Profile.objects.get(id = id)
   person.delete()
   return redirect(profile)
def register(request):
    if request.method=="POST":
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        email = request.POST.get('email')
        # phonenumber = request.POST.get('phoneno')
        password1 = request.POST.get('pass')
        cpassword = request.POST.get('cpass')
        if password1==cpassword:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect(index)
            else:
                user=User.objects.create_user(username=email,first_name=firstname,last_name=lastname,email=email,password=password1)
                Log_User=authenticate(username=email,password=password1)
                auth.login(request,user)
                messages.success(request, 'Form submitted successfully...')
                return redirect(index)
        else:
            messages.error(request, 'Password and confirm passwords are not matched...!!!')
            return redirect(index)
    else:
        return render(request, 'index.html')
def login(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        raw_password=request.POST.get('upass')
        user=auth.authenticate(username=uname,password=raw_password)
        if user is not None:
            auth_login(request,user)
            messages.success(request, 'Logined......!!!!')
            return redirect(index)
        else:
            messages.error(request, 'Invalid credentials.....!!!')
            return redirect(index)
    else:
        return redirect(login)
def logout(request):
    auth_logout(request)
    return redirect(index)