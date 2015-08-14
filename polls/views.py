from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core.servers.basehttp import FileWrapper

import os
import mimetypes

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
    file_path = os.path.dirname(__file__) + '/apk/'  + apk
    original_filename = file_path
    fp = open(file_path, 'rb')
    response = HttpResponse(fp.read())
    fp.close()
    type, encoding = mimetypes.guess_type(original_filename)
    if type is None:
        type = 'application/octet-stream'
    response['Content-Type'] = type
    response['Content-Length'] = str(os.stat(file_path).st_size)
    if encoding is not None:
        response['Content-Encoding'] = encoding
        
    # To inspect details for the below code, see http://greenbytes.de/tech/tc2231/
    if u'WebKit' in request.META['HTTP_USER_AGENT']:
        # Safari 3.0 and Chrome 2.0 accepts UTF-8 encoded string directly.
        filename_header = 'filename=%s' % original_filename.encode('utf-8')
    elif u'MSIE' in request.META['HTTP_USER_AGENT']:
        # IE does not support internationalized filename at all.
        # It can only recognize internationalized URL, so we do the trick via routing rules.
        filename_header = ''
    else:
        # For others like Firefox, we follow RFC2231 (encoding extension in HTTP headers).
        filename_header = 'filename*=UTF-8\'\'%s' % urllib.quote(original_filename.encode('utf-8'))

    response['Content-Disposition'] = 'attachment; ' + filename_header
    return response
    # Create your views here.
