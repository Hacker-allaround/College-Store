from django.db import models
from django.urls import reverse


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    Hod = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='department', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'department'
        verbose_name_plural = 'departments'

    def get_url(self):
        return reverse('storeapp:deptdetail',args=[self.slug])

    def __str__(self):
        return '{}' .format(self.name)
class Course(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='course', blank=True)
    Seat_availability = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'course'
        verbose_name_plural = 'courses'

    def get_url(self):
        return reverse('storeapp:coursedetail',args=[self.department.slug,self.slug])


    def __str__(self):
        return '{}' .format(self.name)

class Material(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Form(models.Model):
    name = models.CharField(max_length=250)
    dob = models.DateField()
    age = models.IntegerField()
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),

    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    mail = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    courses = models.ForeignKey(Course, on_delete=models.CASCADE)
    PURPOSE_CHOICES = [
        ('enquiry', 'For Enquiry'),
        ('order', 'Place Order'),
        ('return', 'Return'),
    ]
    purpose = models.CharField(max_length=10, choices=PURPOSE_CHOICES)
    material_provided = models.ManyToManyField(Material)



    class Meta:
        ordering = ('name',)
        verbose_name = 'form'
        verbose_name_plural = 'forms'


def __str__(self):
        return '{}'.format(self.name)



