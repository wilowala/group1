from django.http import HttpResponse

def contact_view(request):
    return HttpResponse("contact app works")