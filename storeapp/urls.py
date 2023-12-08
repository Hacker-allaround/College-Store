from django.urls import path
from . import views
app_name='storeapp'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('form/',views.form,name='form'),
    path('<slug:c_slug>/', views.deptdetail, name='deptdetail'),
    path('<slug:c_slug>/<slug:course_slug>/', views.coursedetail, name='coursedetail'),
    path('', views.deptdetail, name='home'),
    path('courses',views.getCourses,name='courses')
]


