from django.contrib.auth.models import User, auth
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from Signup_App.forms import UserCreationForm, CategoryForm, BlogForm
from django.contrib.auth.decorators import login_required
from Signup_App.models import *
from django.contrib.auth.decorators import login_required
from .filters import BlogFilterForm_filter

def post(request):
    text = "hajj"
    return HttpResponse(text)


def Home(request):
    return render(request, 'home.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def Logout(request):
    auth.logout(request)
    return redirect('/login/')


def Register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                user_type = request.POST['user_type']
                image = request.FILES.get('image')
                state = request.POST['state']
                district = request.POST['district']
                pin_code = request.POST['pin_code']
                address = request.POST['address']
                newUserDetails = User_details_Model(user_type=user_type, image=image, state=state,
                                                    district=district, pin_code=pin_code,
                                                    address=address, user=user)
                user.save()
                newUserDetails.save()
                return redirect('/login/')
        else:
            messages.info(request, 'password not matching')
            return render(request, "Register.html")
        return redirect('/')
    else:
        return render(request, 'Register.html')


@login_required(login_url="/login/")
def ShowUserData(request):
    data = User_details_Model.objects.filter(user=request.user)
    return render(request, "show_details.html", {'data': data})


def BlogFormView(request):
    form = BlogForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = BlogForm()
    return render(request, 'PostForm.html', {"form": form})


def ShowMyBlogView(request):
    data = BlogModel.objects.filter(user=request.user)
    return render(request, "MyPosts.html", {'data': data})


def ShowFullBlog(request, id):
    da = BlogModel.objects.filter(id=id)
    return render(request, "Post.html", {'da': da})


def ShowAllBlog(request):
    data = BlogModel.objects.all()
    data_filter = BlogFilterForm_filter(request.GET, queryset=data)
    return render(request, "AllPosts.html", {'data': data, 'filter': data_filter})

