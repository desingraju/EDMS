from django.shortcuts import redirect, render
from app.forms import EmployeeFrom
from app.models import Employee
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
@login_required
def home(request):
    employees= Employee.objects.all()
    return render(request,'app/home.html',{'employees':employees})
def detail(request,id):
    employee=Employee.objects.get(id=id)
    return render(request,'app/employee_detail.html',{'employee':employee})
def add_employee(request):
    if request.method=='POST':
       form=EmployeeFrom(request.POST)
       if form.is_valid():
           form.save()
           return redirect('employee_success')
    else:    
      form=EmployeeFrom()
    return render(request,'app/add_employee.html',{'form':form})
def success_view(request):
        return render(request,'app/success.html')
def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid:
           form.save()
           return redirect('login')   
    else:  
        form=UserCreationForm()
    return render(request,'app/register.html',{'form':form})