from django import forms
from .models import Employee, Guest, Member, MemberEntry, GuestEntry

# Create custom widget in your forms.py file.
class DateInput(forms.DateInput):
    input_type = 'date'

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'phone', 'email', 'age', 'gender', 'plan', 'joindate', 'expiredate', 'initialamount']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'phone', 'email', 'age', 'gender', 'startdate']

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['name', 'phone', 'email', 'age', 'gender', 'date', 'price']

class MemberEntryForm(forms.ModelForm):
    class Meta:
        model = MemberEntry
        fields = ['member', 'date']
