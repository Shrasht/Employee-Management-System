from django.shortcuts import render
from .models import Employee,Department,Role
from datetime import datetime
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,'index.html')

def add(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        dept=int(request.POST['dept'])
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        role=int(request.POST['role'])
        phone=int(request.POST['phone'])
        
        new_emp=Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,dept_id = dept,role_id=role,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("ADDED SUCCESSFULLY")
    elif request.method=="GET":
        return render(request,'add.html')
    else:
        return HttpResponse("Exception Occurred")

def delete(request,emp_id=0):
     if emp_id:
         try:
             emp_to_be_removed=Employee.objects.get(id=emp_id)
             emp_to_be_removed.delete()
             return HttpResponse("EMPLOYEE REMOVED SUCCESSFULLY")
             
         except:
             return HttpResponse("Enter a valid Emp ID")
     emps=Employee.objects.all()
     context={
        'emps':emps
    }
     return render(request,'del.html',context)

def all(request):
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,'all.html',context)

def filter(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dept = request.POST.get('dept')
        role = request.POST.get('role')
        emps = Employee.objects.all()

        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name__icontains=dept)
        if role:
            emps = emps.filter(role__name__icontains=role)
        
        context = {
            'emps': emps
        }
        return render(request, 'all.html', context)
    elif request.method == "GET":
        return render(request, 'filter.html')
    else:
        return HttpResponse("INVALID REQUEST")
