import json

from django.contrib import messages
from django.contrib.auth.models import auth,User
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Department,Course,Form
from .forms import FormsForm

# Create your views here.


def deptdetail(request, c_slug=None):
    c_page = None
    course_list = None
    if c_slug is not None:
        c_page = get_object_or_404(Department, slug=c_slug)
        course_list = Course.objects.all().filter(department=c_page, available=True)
    else:
        course_list = Course.objects.all().filter(available=True)

    paginator = Paginator(course_list, 5)

    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        page = 1

    try:
        course_list = paginator.page(page)
    except (EmptyPage, InvalidPage):
        course_list = paginator.page(paginator.num_pages)

    return render(request, 'department.html', {'department': c_page, 'course_list': course_list})


def coursedetail(request,c_slug,course_slug):
    try:
        course=Course.objects.get(department__slug=c_slug,slug=course_slug)
    except Exception as e:
        raise e
    return render(request,'course.html',{'course':course})


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid password / username')
            return redirect('storeapp:login')


    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method=='POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['confirm_password']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('storeapp:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already taken')
                return redirect('storeapp:register')

            else:
                user = User.objects.create_user(username=username, password=password, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save();
                return redirect('storeapp:login')
        else:
            messages.info(request, 'password not match')
            return redirect('storeapp:register')
        return redirect('/')
    return render(request,'register.html')

def form(request):
    form = FormsForm()
    if request.method == "POST":
        form = FormsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order Confirmed!')
        else:
            print(form.errors)
            messages.error(request,'Form submission failed, select any material field ')
    return render(request,'form.html',{'form': form})

def getCourses(request):
    data = json.loads(request.body)
    department_id = data["id"]
    courses = Course.objects.filter(department__id=department_id)
    return JsonResponse(list(courses.values("id","name")),safe=False)




