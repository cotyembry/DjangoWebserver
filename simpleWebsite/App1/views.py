from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime

# Create your views here.


# this works
#
def index(request):
	# content = '<html>test123</html>'

	# response = HttpResponse(content, content_type='application/liquid')
	# response['Content-Length'] = len(content)

	# return response


					# <script src=\"https://raw.githubusercontent.com/cotyembry/DjangoWebserver/master/simpleWebsite/App1/templates/index.html\"></script>\

	html = "<html>\
				<body>\
					<script src=\"http://rawgit.com/cotyembry/DjangoWebserver/master/simpleWebsite/App1/templates/index.html\"></script>\
				</body>\
			</html>"

	response = HttpResponse(html, content_type='text/html')
	response['Content-Length'] = len(html)

	return response


# def index(request):
#     return HttpResponse("Boom, in App1 app's index view")


# I could not figure out how to get this to work - this requires more configuration
#
# def index(request):
#     return render_to_response('D:\\Developer\\DjangoWebserver\\simpleWebsite\\index.html')
#     # return render_to_response('simpleWebsite/index.html')



