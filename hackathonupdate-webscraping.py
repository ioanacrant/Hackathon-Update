from lxml import html
import requests


page=requests.get('https://mlh.io/seasons/s2015/events.html')
tree=html.fromstring(page.text)


titles=tree.xpath('//*[name()="h3"]/text()')
#add dates and locations later

print(titles)