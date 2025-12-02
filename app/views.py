from django.shortcuts import redirect, render
from app.forms import EmployeeFrom
from app.models import Employee
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
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
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        try:
            if form.is_valid():
                form.save()
                messages.success(
                    request,
                    "Account created successfully. You can now log in."
                )
                return redirect('login')
            else:
                messages.error(
                    request,
                    "Registration failed. Please correct the errors below."
                )

        except Exception as e:
            print("Registration error:", e)
            messages.error(
                request,
                "Something went wrong. Please try again later."
            )
    else:
        form = UserCreationForm()
    return render(request, 'app/register.html', {'form': form})

