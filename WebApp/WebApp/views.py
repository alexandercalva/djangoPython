
from django.http import HttpResponse

def regards(request): #first view
    return HttpResponse("Hello World Django") 
