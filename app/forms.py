from app.models import Employee
from django import forms
class EmployeeFrom(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'