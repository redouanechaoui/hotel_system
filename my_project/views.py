from django.http import HttpResponse

def WelcomePage(request):
    return HttpResponse("welcome to our system")