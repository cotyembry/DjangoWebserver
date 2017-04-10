from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime

# Create your views here.


def index(request):
    return render_to_response('D:\\Developer\\DjangoWebserver\\simpleWebsite\\index.html')
    # return render_to_response('simpleWebsite/index.html')

# def index(request):
#     return HttpResponse("Boom, in App1 app's index view")


# this works
#
# def index(request):
#     now = datetime.datetime.now()
#     html = "<html><body><b>It is now %s.</b></body></html>" % now
#     return HttpResponse(html)
