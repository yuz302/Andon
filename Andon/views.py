from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.template import Template, Context
import urllib2
import re
import datetime

# Create your views here.

def index(request):

    template = loader.get_template('Andon/index.html')
    context = Context({"prod_name": getProductName(getHtml('http://10.10.10.123/user/andon.htm'))[0], "prod_batch_num": getProductBatchNumber(getHtml('http://10.10.10.123/user/andon.htm'))[0]})

    #context2 = Context({"prod_name": "AB1234", "prod_batch_num": "87654321"}) # one template, multiple contexts
    return HttpResponse(template.render(context))   # the template after rendering
    # return render(request, 'Andon/index.html', context)

def curr_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s. </body></html>" % now
    return HttpResponse(html)


def getHtml(url):
    response = urllib2.urlopen(url)
    html = response.read()
    return html


def getProductName(html):
    prod_re = r'<p id="prod">(.*?)</p>'
    prod_match = re.findall(prod_re, html,re.S|re.M)
    return prod_match


def getProductBatchNumber(html):
    prod_re = r'<p id="prodbatch">(.*?)</p>'
    prod_match = re.findall(prod_re, html, re.S | re.M)
    return prod_match

if __name__ == '__main__':
    url = 'http://10.10.10.123/user/andon.htm'
    html = getHtml(url)
    productname = getProductName(html)[0]
    productbatchnumber = getProductBatchNumber(html)[0]