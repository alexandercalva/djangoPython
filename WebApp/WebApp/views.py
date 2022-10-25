
import datetime
from django.http import HttpResponse

def regards(request): #first view
    return HttpResponse("Hello World Django") 

def dateNow(request):
    date_now = datetime.datetime.now()
    document = """
    <html>
    <body>
    <h1>
    Currently date and time %s
    </h1>
    </body>
    </html>""" % date_now

    return HttpResponse(document)
