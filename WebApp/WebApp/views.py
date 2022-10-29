
from django.template import Template, Context
from django.http import HttpResponse
from django.db import models
from django.shortcuts import redirect

def regards(request): #first view
    return HttpResponse("Hello World Django") 

def web_page(request):
    doc_externo = open("C:/Users/Alexander/Documents/BYU/BYU-Alex/CSE310/djangoPython/WebApp/WebApp/templates/plantilla.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    document = plt.render(ctx)
    return HttpResponse(document)

def register_client(request):
    name = request.GET['name']
    email = request.GET['email']
    subject = request.GET['subject']
    message = request.GET['message']

    clients = models.Client.objects.create(
        name = name,
        email = email,
        subject = subject,
        message = message
    )
    return redirect('/')