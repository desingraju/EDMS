from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from app.forms import EmployeeFrom
from app.models import Employee


@login_required
def home(request):
    employees = Employee.objects.all()
    return render(request, 'app/home.html', {'employees': employees})


def detail(request, id):
    # safer than Employee.objects.get(id=id)
    employee = get_object_or_404(Employee, id=id)
    return render(request, 'app/employee_detail.html', {'employee': employee})


def add_employee(request):
    if request.method == 'POST':
        form = EmployeeFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_success')
    else:
        form = EmployeeFrom()

    return render(request, 'app/add_employee.html', {'form': form})


def success_view(request):
    return render(request, 'app/success.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():                      # ✅ correct usage
            form.save()
            messages.success(
                request,
                "Account created successfully. You can now log in."
            )
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'app/register.html', {'form': form})
