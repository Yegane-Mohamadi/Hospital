# forms.py
from django import forms
from .models import Employee, Shift

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'hospital_name', 'job']

class ShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = ['employee', 'date', 'shift_time']
