from re import A
from .models import *
from django.http import Http404
from django.shortcuts import render, redirect
from .forms import AppointmentForm


































































































































def available(request):
    doctors = Profle.objects.all().filter(roles='Dr')


    context = {'doctors': doctors}
    return render(request,'pet/available.html', context=context)

def booking(request,drName):
    form = AppointmentForm(request.POST)
    context = {'form': form}
    try:
        doctor = Profle.objects.get(name=drName)
    except Profle.DoesNotExist:
        return Http404
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
          new_appointment = Appointment(pet_owner=request.user, doctor=doctor, time=form.cleaned_data['time'], date=form.cleaned_data['date'])
          new_appointment.save()




          return render(request,'pet/booking.html')
        return render(request,'pet/booking.html')
    return render(request,'pet/booking.html',context=context)