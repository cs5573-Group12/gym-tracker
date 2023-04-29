from django.utils import timezone
from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponse

from gym.forms import EmployeeForm
from gym.models import Employee

from guests.models import Guest
from members.models import Member, MemberEntry
# from app.members.models import MemberEntry

from app.settings import TIME_ZONE
# Create your views here.
def index(request):
    """
    Show landing page
    """
    # Get initial data

    # Get the current timezone
    current_timezone = timezone.get_current_timezone()
    print("Current timezone:", current_timezone)

    print("settings.TIME_ZONE: ", TIME_ZONE)
    today = datetime.now().date()
    aware_today = timezone.make_aware(datetime.combine(today, datetime.min.time()), timezone.get_current_timezone())
    print("right now: ", aware_today)
    
    
    total_entries_today = []
    member_entries_today, guest_entries_today = [], []

    member_entries_today = MemberEntry.objects.filter(date__date=aware_today.date())
    
    guest_entries_today = Guest.objects.filter(date__date=aware_today.date())
    
    print("guest_entries_today:", guest_entries_today)

    # 
    for entry in member_entries_today:
        print("entry: ", entry.date.isoformat())
        normalized_entry = {
            "name": entry.member.name,
            "type": "member",
            "checked_in_by": entry.checked_in_by.username,
            "date": entry.date.time()
        }
        total_entries_today.append(normalized_entry)

    for entry in guest_entries_today:
        normalized_entry = {
            "name": entry.name,
            "type": "guest",
            "checked_in_by": entry.checked_in_by.username,
            "date": entry.date.time()
        }
        total_entries_today.append(normalized_entry)

    context = {
        'url': request.get_full_path(),
        "member_entries": member_entries_today, 
        "guest_entries": guest_entries_today,
        "total_entries": total_entries_today
    }
    return render(request, "index.html", context)

    
def employees(request):
    view_all_employees = Employee.objects.all().order_by('name')
    print(request.get_full_path())
    context = {
        'url': request.get_full_path(),
        'employees': view_all_employees,
        'employees_count': view_all_employees.count()
    }
    return render(request, 'employees.html', context)

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            newEmployee = form.save(commit=False)

            newEmployee.save()
            return redirect('employees')
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})

def edit_employee(request, employee_id):
    try:  
      employee = get_object_or_404(Employee, id=employee_id)
    except Http404:
      return redirect('employees')
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employees')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'edit_employee.html', {'form': form})

def delete_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    employee.delete()
    return redirect('employees')


def transactions(request):
    context = {
        'url': request.get_full_path(), 
    }
    return render(request, 'transactions.html', context)

def settings(request):
    context = {
        'url': request.get_full_path(), 
    }
    return render(request, 'settings.html', context)

def contact(request):
    context = {
        'url': request.get_full_path(), 
    }
    return render(request, 'contact.html', context)

def about(request):
    context = {
        'url': request.get_full_path(), 
    }
    return render(request, 'about.html', context)