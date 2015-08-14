from django.http import HttpResponse
from django.template import RequestContext, loader
import os

def index(request):
    apk_dir = os.path.dirname(__file__) + "/apk"
    apk_list = list();
    if(os.path.exists(apk_dir)):
        for root,dirs,files in os.walk(apk_dir):
            for file in files:
                if(file.endswith('.apk')):
                    apk_list.append(file)

    context = RequestContext(request,{
        'apk_list' : apk_list,
    })
    template = loader.get_template('polls/index.html')
    return HttpResponse(template.render(context))

def detail(request,question_id):
    return HttpResponse("You're looking at question.")

def apk_detail(request,apk):
    return HttpResponse(os.path.dirname(__file__) + "/apk/" + apk)

    # Create your views here.
