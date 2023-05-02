from django.utils import timezone
from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponse

from gym.forms import EmployeeForm
from gym.models import Employee

from django.contrib.auth.models import User
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
    today = datetime.now().date()
    aware_today = timezone.make_aware(datetime.combine(today, datetime.min.time()), timezone.get_current_timezone())

    
    total_entries_today = []
    member_entries_today, guest_entries_today = [], []

    member_entries_today = MemberEntry.objects.filter(date__date=aware_today.date())
    
    guest_entries_today = Guest.objects.filter(date__date=aware_today.date())
    
    # 
    for entry in member_entries_today:
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

    # print("total_entries_today: ", total_entries_today)

    # Initialize dictionaries to keep track of counts by hour for each type
    data = []
    
    # Initialize dictionary to keep track of counts by hour and type
    counts_by_hour_and_type = {}

    # Loop through entries and increment counts in dictionary
    for entry in total_entries_today:
        hour = entry['date'].hour
        if hour in counts_by_hour_and_type:
            counts_by_hour_and_type[hour]['total'] += 1
            if entry['type'] == 'member':
                counts_by_hour_and_type[hour]['member'] += 1
            elif entry['type'] == 'guest':
                counts_by_hour_and_type[hour]['guest'] += 1
            counts_by_hour_and_type[hour]['label'] = f"Member: {counts_by_hour_and_type[hour]['member']}, Guest: {counts_by_hour_and_type[hour]['guest']}"
        else:
            counts_by_hour_and_type[hour] = {
                "hour": hour,
                "total": 1,
                "member": 1 if entry['type'] == 'member' else 0,
                "guest": 1 if entry['type'] == 'guest' else 0,
                "label": f"Member: {1 if entry['type'] == 'member' else 0}, Guest: {1 if entry['type'] == 'guest' else 0}"
            }

    # print("counts_by_hour_and_type: ", counts_by_hour_and_type)
    hours = range(0, 24)
    for hour in hours:
        if hour not in counts_by_hour_and_type:
            counts_by_hour_and_type[hour] = {
                "hour": hour,
                "total": 0,
                "member": 0,
                "guest": 0,
                "label": f"Member: {0}, Guest: {0}"
            }
    # print("hours: ", hours)
    # print("counts_by_hour_and_type: ", counts_by_hour_and_type)
    # Convert dictionary to list
    counts_list = list(counts_by_hour_and_type.values())

    # Sort list by hour
    counts_list.sort(key=lambda x: x['hour'])


    # Print out list
    for item in counts_list:
        military_time = f"{item['hour']}:00:00"
        am_pm_time = datetime.strptime(military_time, "%H:%M:%S").strftime("%I:%M %p")
        item['hour'] = am_pm_time
    
    context = {
        'url': request.get_full_path(),
        "member_entries": member_entries_today, 
        "guest_entries": guest_entries_today,
        "total_entries": total_entries_today,
        "data1": counts_list,
        "data": [item['total'] for item in counts_list],
        "dataLabels": [item['label'] for item in counts_list],
        "labels": [item['hour'] for item in counts_list],
    }
    return render(request, "index.html", context)

    
def employees(request):
    view_all_employees = User.objects.all()

    # id
    # password
    # last_login
    # is_superuser
    # username
    # first_name
    # last_name
    # email
    # is_staff
    # is_active
    # date_joined
    # groups
    # user_permissions
    
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