from django.contrib import admin

# Register your models here.
from .models import Employee,Department,Role

admin.site.register(Employee),
admin.site.register(Department),
admin.site.register(Role)

class EmpAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','dept','salary', 'bonus', 'role', 'phone','hire_date']


