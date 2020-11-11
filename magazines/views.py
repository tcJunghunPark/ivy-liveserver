from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



from .models import *
from .forms import CreateUserForm


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form':form}
        return render(request, 'magazines/register.html', context)

def loginPage(request):

    if request.user.is_authenticated:
        return redirect('home')
    
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')
        context = {}
        return render(request, 'magazines/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

# Create your views here.
def home(request):
    context = {}
    return render(request, 'magazines/homepage.html', context)

def loginHome(request):
    context = {}
    return render(request, 'magazines/loginHome.html', context)

def blog(request):
    context = {}
    return render(request, 'magazines/blog.html', context)

@login_required(login_url = 'login')
def portfolio(request):

    sort = request.GET.get('sort','')
    print(sort)

    if sort == 'date':
        posts = Post.objects.order_by('-date_created')
    elif sort == 'title':
        posts = Post.objects.order_by('title')
    elif sort == 'mostView':
        posts = Post.objects.order_by('-viewcount')
    else:
        posts = Post.objects.all()

    context = {'posts':posts}
    return render(request, 'magazines/portfolio.html', context) 

@login_required(login_url = 'login')
def detail_view(request, id):
    post = get_object_or_404(Post, id=id)
    photos = PostImage.objects.filter(post=post)
    context = {
        'post':post,
        'photos':photos
    }
    return render(request, 'magazines/detail.html', context)


@login_required(login_url = 'login')
def magazine(request):
    magazine = Magazine.objects.all()
    magazine = sorted(magazine,key = lambda x : x.date_created)
    return render(request, 'magazines/magazine.html', {'magazine':magazine})

@login_required(login_url = 'login')
def viewMagazine(request,pk):
    magazine = Magazine.objects.get(id=pk)
    for i in request.user.groups.all():
        print(type(i))
        print(i.name)
        if magazine.magazineGroup == i.name or i.name == 'admin':
            return render(request, 'magazines/viewMagazine.html', {'magazine':magazine})

    return render(request, 'magazines/magazine_access_denied.html',{'magazine':magazine})
    
    # return render(request, 'magazines/viewMagazine.html', {'magazine':magazine})
    
def aboutUs(request):
    context = {}
    return render(request, 'magazines/aboutUs.html', context)

def contactUs(request):
    if request.method == 'POST':
        if "message-submit" in request.POST:
            message_name = request.POST["message-name"]
            message_email = request.POST["message-email"]
            message_subject = request.POST["message-subject"]
            message_info = request.POST["message-info"]

            message_content = 'Subject: ' + message_subject + '\nUser Name: ' + message_name + '\nUser Email: ' + message_email + '\nMessage: ' + message_info
                        
            # send an email
            send_mail(
                'IVY Contact Us message sent by ' + message_name, # subject
                message_content,                   # message
                settings.EMAIL_HOST_USER,          # from email
                [settings.EMAIL_HOST_USER]       # to email
            
            )
        if "purchase-submit" in request.POST:
            purchase_name = request.POST["purchase-name"]
            purchase_email = request.POST["purchase-email"]
            purchase_magazine_list = request.POST.getlist('magazine-list')
            purchase_magazines = ""
            for magazine in purchase_magazine_list:
                if not purchase_magazines:
                    purchase_magazines += magazine
                else:
                    purchase_magazines += ' ,' + magazine
            purchase_content = 'IVY Magazine Purchase Request ' + '\nUser Name: ' + purchase_name + '\nUser Email: ' + purchase_email + '\nMagazines to buy: ' + purchase_magazines
            
            send_mail(
                    'IVY Magazine purchase request from ' + purchase_name, # subject
                    purchase_content,                 
                    settings.EMAIL_HOST_USER,          # from email
                    [settings.EMAIL_HOST_USER]       # to email
                
                )
    context = {}
    return render(request, 'magazines/contactUs.html', context)

@login_required(login_url = 'login')
def info(request):
    context = {}
    return render(request, 'magazines/info.html', context)

def signIn(request):
    context = {}
    return render(request, 'magazines/signIn.html', context)

def signUp(request):
    context = {}
    return render(request, 'magazines/signUp.html', context)

def magazineAccessDenied(request):
    context = {}
    return render(request, 'magazines/magazine_access_denied.html', context)