from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponse

from members.forms import MemberEntryForm, MemberForm
from members.models import Member

# Create your views here.
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