from django.shortcuts import render
from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponse

from .models import Guest
from .forms import GuestForm

# Create your views here.
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
            newGuest.checked_in_by = request.user
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