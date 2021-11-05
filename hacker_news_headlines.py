from email.mime.nonmultipart import MIMENonMultipart
import requests # http requests

from bs4 import BeautifulSoup # web scraping and Send the mail

import smtplib # email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# system date and time manipulation
import datetime
now = datetime.datetime.now()

#email content placeholder

content = ''

def extract_news(url):
    print('Extracting Hacker News Stories...')
    cnt = ''
    cnt +=('<b>HN Top Stories:<b>\n'+ '<br>'+ '-'*50+ '<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,'html.parser')
    for i,tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
        cnt += ((str(i+1)+' :: '+ tag.text+ '\n'+ '<br>') if tag.text != 'More' else '')
        #print(tag.prettify) #find_all('span',attr={'class':'sitestr'})
    return cnt

cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>------<br>')
content += ('<br><br>End of Message<br>')

#lets send the email
print('Composing Email...')

#update email details
SERVER = 'smtp.gmail.com' # "your smtp server"
PORT = 587 # your port number
FROM = ''
TO = ''
PASS = '' # password

# fp = open(file_name, 'rb')
# Create a text/plain message
# msg = MIMEText('')
msg = MIMEMultipart()

# msg.add_header('Content-Diaposition', 'attachment', filename='empty.txt')
msg['Subject'] = 'Top News Stories HN [Automated Email]'+ ' '+ str(now.day)+\
    '-'+ str(now.month)+ '-'+ str(now.year)
msg['FROM'] = FROM
msg['TO'] = TO

msg.attach(MIMEText(content,'html'))
# fp.close()

print('Initiating Server...')

server = smtplib.SMTP(SERVER, PORT)
# server = smtplib.SMTP SSL('smtp.gmail.com', 465)
server.set_debuglevel(1) # 1 -> error mssgs, 0 -> no mssgs
server.helo()
server.starttls()
server.login(FROM,PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email Sent...')
server.quit()
