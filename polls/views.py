from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
    apk_list = {'1','2','3'}
    context = RequestContext(request,{
        'apk_list' : apk_list,
    })
    template = loader.get_template('polls/index.html')
    return HttpResponse(template.render(context))

def detail(request,question_id):
    return HttpResponse("You're looking at question.")

    # Create your views here.
