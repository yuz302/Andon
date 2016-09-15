from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.template import Template, Context
import urllib2
import re
import datetime

# This python file renders html templates with real-time preblend information via simple web scraping functions
# It requests html files created by Phil on blender HMI servers and uses regular expression to parse those html files
# to get real-time product name, product batch number, raw material name and raw material batch number for each blender
# Diana Zhou
# 09/15/2016

# declare url strings
url32 = 'http://10.10.10.123/user/andon.htm'


# As urls.py configured, this index function is called when a user enters IP address in the browser
def index(request):

    # load template html for the Andon board page
    template = loader.get_template('Andon/index.html')

    # fetch information from HMIs and store them in dictionary
    html32 = get_html(url32)

    context = Context({
        "datetime": datetime.datetime.now(),
        "prod_name3": get_product_name(html32),
        "prod_batch_num3": get_product_batch_number(html32),
        "rm_name3": get_rm_name(html32),
        "rm_batch_number3": get_rm_batch_number(html32)
    })

    # render the templates and return
    return HttpResponse(template.render(context))   # the template after rendering


# below function is not in use. It's just a sample for how to get date and time with python built-in package
def curr_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s. </body></html>" % now
    return HttpResponse(html)


# the function to request html file from url
def get_html(url):
    try:
        response = urllib2.urlopen(url)
        html = response.read()
    except ValueError:
        return None
        pass
    return html


# below functions take html files and return variables by matching regular expression
def get_product_name(html):
    if html is None:
        return "Can't access to HMI page. "
    prod_re = r'<p id="prod">(.*?)</p>'
    prod_match = re.findall(prod_re, html,re.S|re.M)
    return prod_match[0]


def get_product_batch_number(html):
    if html is None:
        return "Can't access to HMI page. "
    prod_re = r'<p id="prodbatch">(.*?)</p>'
    prod_match = re.findall(prod_re, html, re.S | re.M)
    return prod_match[0]


def get_rm_name(html):
    if html is None:
        return "Can't access to HMI page. "
    rm_re = r'<p id="raw">(.*?)</p>'
    rm_match = re.findall(rm_re, html, re.S | re.M)
    return rm_match[0]


def get_rm_batch_number(html):
    if html is None:
        return "Can't access to HMI page. "
    rm_batch_re = r'<p id="rawbatch">(.*?)</p>'
    rm_batch_match = re.findall(rm_batch_re, html, re.S | re.M)
    return rm_batch_match[0]
