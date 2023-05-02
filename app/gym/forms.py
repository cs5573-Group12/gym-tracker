from django import forms
from .models import Employee

# Create custom widget in your forms.py file.
class DateInput(forms.DateInput):
    input_type = 'date'

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'phone', 'email', 'age', 'gender', 'startdate']
