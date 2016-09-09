from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.template import Template, Context

from Andon.models import Product
import datetime

# Create your views here.

def index(request):

    template = loader.get_template('Andon/index.html')
    context = Context({"prod_name": "AB1234", "prod_batch_num": "87654321"})

    context2 = Context({"prod_name": "AB1234", "prod_batch_num": "87654321"}) # one template, multiple contexts
    return HttpResponse(template.render(context))   # the template after rendering
    # return render(request, 'Andon/index.html', context)

def curr_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s. </body></html>" % now
    return HttpResponse(html)