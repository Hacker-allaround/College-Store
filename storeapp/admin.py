from django.contrib import admin

# Register your models here.
from . models import Department,Course,Form,Material

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Department,DepartmentAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'department', 'Seat_availability', 'available', 'created', 'updated']
    list_editable = ['Seat_availability', 'available']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20
admin.site.register(Course,CourseAdmin)

class FormAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'age', 'department', 'courses', 'purpose', 'mail', 'phone_number']
    list_per_page = 20
admin.site.register(Form,FormAdmin)

class MaterialAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Material, MaterialAdmin)