from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponse

from gym.models import Employee, Guest, Member, MemberEntry, GuestEntry
from gym.forms import MemberForm, EmployeeForm, GuestForm, MemberEntryForm

# Create your views here.
def index(request):
    """
    Show landing page
    """
    # Get initial data
    today = datetime.now().strftime("%Y-%m-%d")
    print("right now: ", datetime.now())
    member_entries_today = MemberEntry.objects.filter(date=today)
    print("first mem entry:", member_entries_today.first().date)
    member_entries = member_entries_today.count()
    guest_entries_today = Guest.objects.filter(date=today)
    guest_entries = guest_entries_today.count()
    

    total_entries_today = []
    for entry in member_entries_today:
        normalized_entry = {
            "name": entry.member.name,
            "type": "member",
            "date": entry.date.strftime("%Y-%m-%d")
        }
        total_entries_today.append(normalized_entry)

    for entry in guest_entries_today:
        normalized_entry = {
            "name": entry.name,
            "type": "guest",
            "date": entry.date.strftime("%Y-%m-%d")
        }
        total_entries_today.append(normalized_entry)

    context = {
        'url': request.get_full_path(),
        "member_entries": member_entries_today, 
        "guest_entries": guest_entries_today,
        "total_entries_today": total_entries_today
    }
    return render(request, "index.html", context)

def members(request):
    view_all_members = Member.objects.all().order_by('name')

    context = {
        'url': request.get_full_path(),
        'members': view_all_members,
        'members_count': view_all_members.count()
    }
    return render(request, 'members.html', context)

def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            newMember = form.save(commit=False)
            newMember.save()
            return redirect('members')
    else:
        form = MemberForm()
    return render(request, 'add_member.html', {'form': form})

def member_detail(request, member_id):
    try:  
      member = get_object_or_404(Member, id=member_id)
    except Http404:
      return redirect('members')
    
    context = {
        'url': request.get_full_path(),
        'member': member
    }
    return render(request, 'member_detail.html', context)

def edit_member(request, member_id):
    try:  
      member = get_object_or_404(Member, id=member_id)
    except Http404:
      return redirect('members')
    print(member)
    
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('members')
    else:
        form = MemberForm(instance=member)
    return render(request, 'edit_member.html', {'form': form})

def delete_member(request, member_id):
    member = Member.objects.get(id=member_id)
    member.delete()
    return redirect('members')

def member_check_in(request):
    if request.method == 'POST':
        form = MemberEntryForm(request.POST)
        if form.is_valid():
            newMemberEntry = form.save(commit=False)
            newMemberEntry.save()
            return redirect('members')
    else:
        form = MemberEntryForm()
    return render(request, 'member_check_in.html', {'form': form})
    
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
        form = MemberForm()
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

def guests(request):
    view_all_guests = Guest.objects.all().order_by('date')

    context = {
        'url': request.get_full_path(),
        'guests': view_all_guests,
        'guests_count': view_all_guests.count()
    }
    return render(request, 'guests.html', context)

def add_guest(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            newGuest = form.save(commit=False)

            newGuest.save()
            return redirect('guests')
    else:
        form = GuestForm()
    return render(request, 'add_guest.html', {'form': form})

def edit_guest(request, guest_id):
    try:  
      guest = get_object_or_404(Guest, id=guest_id)
    except Http404:
      return redirect('guests')
    
    if request.method == 'POST':
        form = GuestForm(request.POST, instance=guest)
        if form.is_valid():
            form.save()
            return redirect('guests')
    else:
        form = GuestForm(instance=guest)
    return render(request, 'edit_guests.html', {'form': form})

def delete_guest(request, guest_id):
    guest = Guest.objects.get(id=guest_id)
    guest.delete()
    return redirect('guests')

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