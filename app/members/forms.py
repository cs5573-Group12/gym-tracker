from django import forms

from .models import Member, MemberEntry

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'phone', 'email', 'age', 'gender', 'plan', 'expiredate', 'initialamount']

class MemberEntryForm(forms.ModelForm):
    class Meta:
        model = MemberEntry
        fields = ['member']
