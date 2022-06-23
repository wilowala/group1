from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.http  import HttpResponse,Http404
from .forms import SignupForm,UpdateProfileForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.contrib import messages
from django.views.generic import ListView, DetailView, TemplateView
from .models import Doctor


class hospitalView(TemplateView):
    template_name = 'index.html'
    
# def hospitalView(request):
#     return render(request, 'index.html')

# def DoctorListView(request):
#     queryset = Doctor.objects.all()
#     return render(request, 'doctor-team.html', {'queryset': queryset})
    


class DoctorListView(ListView):
    queryset = Doctor.objects.all()
    template_name = 'doctor-team.html'



class ContactView(TemplateView):
    template_name = 'contact.html'
    
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email_from = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if subject == '':
            subject = 'Healthcae Contact'     

        if name and message and email_from:
            send_mail(
                subject+ " - " + name,
                message+ 
                email_from,
                ['yourname@gmail.com',],
                fail_silently=False,
            )
            messages.success(request, f'Your message has been sent. Thank you {name}!')

        return redirect('contact')




@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'home.html')

def profile(request, username):
    return render(request, 'profile.html')

def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile', user.username)
    else:
        form = UpdateProfileForm()
    return render(request, 'editprofile.html', {'form': form})


