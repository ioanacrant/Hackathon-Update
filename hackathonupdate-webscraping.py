from lxml import html
import requests
import sendgrid

sguser="djsgkjg"
sgpass="fdggfd"
inf= open("output.txt")
oldhackathons=inf.readlines()
inf.close()

outf=open("output.txt","w")

reqpage='https://mlh.io/seasons/f2015/events.html'
page=requests.get(reqpage)
tree=html.fromstring(page.text)

def get_hackathon_names():
    titles=tree.xpath('//*[name()="h3"]/text()')
    return titles
#add dates and locations later

newhackathons=get_hackathon_names()

if len(oldhackathons)!=len(newhackathons):
    addedhackathons=list(set(newhackathons)-set(oldhackathons))

    sg = sendgrid.SendGridClient(sguser, sgpass)
    message = sendgrid.Mail()
    message.add_to("ioana.crant@gmail.com")
    message.set_from("hackathon.update@gmail.com")
    message.set_subject("Some hackathons have been added to MLH!")
    message.set_html("Hey, check out MLH.io!")

    sg.send(message)

outf.write ("\n".join(newhackathons))
outf.close()
