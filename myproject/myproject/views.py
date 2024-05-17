from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Hello, World!")

def about(request):
    return HttpResponse("About me")
