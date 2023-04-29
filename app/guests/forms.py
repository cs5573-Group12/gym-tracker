from django import forms
from .models import Guest

# Create custom widget in your forms.py file.
class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['name', 'phone', 'email', 'age', 'gender', 'price']

