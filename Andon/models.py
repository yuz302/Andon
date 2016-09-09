from __future__ import unicode_literals

from django.db import models
import urllib2
import re

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    batch_number = models.CharField(max_length=200)

    def __init__(self, name, batchnumber):
        self.name = name
        self.batch_number = batchnumber

    def get_name(self):
        return self.name

    def get_batch_number(self):
        return self.batch_number

x = Product("PH1234", "12345678")
print(x.get_batch_number())


# below is the web scraping logic

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
    print getProductName(html)[0]
    print getProductBatchNumber(html)[0]
