from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
    template = loader.get_template('polls/index.html')
    return HttpResponse(template.render())

def detail(request,question_id):
    return HttpResponse("You're looking at question.")

    # Create your views here.
