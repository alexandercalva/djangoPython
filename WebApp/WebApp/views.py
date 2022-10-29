
import datetime
from django.template import Template, Context
from django.http import HttpResponse

def regards(request): #first view
    return HttpResponse("Hello World Django") 

def dateNow(request):
    doc_externo = open("C:/Users/Alexander/Documents/BYU/BYU-Alex/CSE310/djangoPython/WebApp/WebApp/templates/plantilla.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    document = plt.render(ctx)
    return HttpResponse(document)
