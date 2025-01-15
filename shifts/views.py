# views.py
from django.shortcuts import render, redirect
from .forms import EmployeeForm, ShiftForm
from .models import Shift

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_shift')
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})

def add_shift(request):
    if request.method == 'POST':
        form = ShiftForm(request.POST)
        if form.is_valid():
            shift = form.save(commit=False)
            # شرط برای جلوگیری از شیفت شب
            if shift.shift_time == 'night' and not shift.employee.can_work_night_shift:
                form.add_error('shift_time', 'This employee cannot work night shifts.')
            else:
                shift.save()
                return redirect('add_shift')
    else:
        form = ShiftForm()
    return render(request, 'add_shift.html', {'form': form})
