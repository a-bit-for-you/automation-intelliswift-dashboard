#This tool is developed by Sachin Gupta. 
#For any suggestion/feedback contact: 7276317717.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
#import pyautogui
import os
import time
from datetime import datetime
from datetime import date
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

x=sys.argv[1]

today=date.today()
dat=today.strftime("%d_%B_%Y")
now=datetime.now()
tim=now.strftime("%H_%M")
#os.system("nmcli con up id shopstyle-vpn-v2")
#print(pyautogui.position())
driver=webdriver.Chrome('/home/intelliswift/tools/selenium/chromedriver')
driver.get('https://admin.shopstyleops.com/Admin/app')
#Login
e=driver.find_element_by_name('TextField')
e.send_keys('sachin.gupta@intelliswift.co.in')
e=driver.find_element_by_name('TextField_0')
e.send_keys('ShopStyle1')
e=driver.find_element_by_id('Submit')
e.click()
driver.maximize_window()

#Remove selenium notification i.e 'Chrome is being controlled'
#will be done in future
#=============================================================

#functions
def button_wait(xpath):
    wait = WebDriverWait(driver, 20)
    e = WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.XPATH, xpath)))
    e.click()
def text_wait(xpath,text):
    wait = WebDriverWait(driver, 20)
    e = WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.XPATH, xpath)))
    e.send_keys(text)
    #e.send_keys(Keys.ENTER)
#=============================================================================================

#crawl code
driver.get('https://admin.shopstyleops.com/Admin/app?page=CrawlerDashboardPage&service=page')#opens the Crawler Dashboard
if x=="sunday":
    e=driver.find_element_by_name('week')
    e.send_keys(Keys.DOWN)
    e.click()
    e.send_keys(Keys.ENTER)
text_wait('//*[@id="inputField"]','nordstrom')#types nordstrom in crawl search box
button_wait('//*[@id="Checkbox"]')#clicks on the checkbox
button_wait('//*[@id="Form"]/input[2]')#clicks on crawl search button
os.system("mkdir /home/intelliswift/tools/selenium/screenshots/dashboard_check_"+dat+"_"+x)
driver.save_screenshot("/home/intelliswift/tools/selenium/screenshots/dashboard_check_"+dat+"_"+x+"/nordstrom_crawl.png")
driver.execute_script("window.open('https://admin.shopstyleops.com/Admin/app?page=RetailerDashboardPage&service=page', 'tab2');")
driver.switch_to.window("tab2")

#import
text_wait('//*[@id="TextField"]','nordstrom')#types nordstrom in the import search box
button_wait('//*[@id="Checkbox"]')#clicks on the checkbox
button_wait('//*[@id="Form"]/input[2]')#clicks on search button
driver.save_screenshot("/home/intelliswift/tools/selenium/screenshots/dashboard_check_"+dat+"_"+x+"/nordstrom_import.png")

li=('Ssense','barneys','netaporter','macys','farfetch','zappos','bloomingdales','bloomingdaleshome','nordstromrack_us','revolveclothing','ruelala_us','shopbop','jcpenney_home','yoox','barneyswarehouse_us','JCPenney')
#li=['Ssense']
for value in li:
    driver.switch_to.window(driver.window_handles[0])#switch to first tab
    driver.find_element_by_xpath('//*[@id="inputField"]').clear()#clears the crawl search box
    text_wait('//*[@id="inputField"]',value)#types site name in crawl search box
    button_wait('//*[@id="Form"]/input[2]')#clicks on crawl search button
    driver.save_screenshot("/home/intelliswift/tools/selenium/screenshots/dashboard_check_"+dat+"_"+x+"/"+value+"_crawl.png")
    driver.switch_to.window(driver.window_handles[1])#switch to second tab
    driver.find_element_by_xpath('//*[@id="TextField"]').clear()#clears the crawl search box
    text_wait('//*[@id="TextField"]',value)#types site name in the import search box
    button_wait('//*[@id="Form"]/input[2]')#clicks on search button
    driver.save_screenshot("/home/intelliswift/tools/selenium/screenshots/dashboard_check_"+dat+"_"+x+"/"+value+"_import.png")
driver.quit()
#os.system("nmcli con down id shopstyle-vpn-v2")
if x=="daily_check":
    toaddr =  "sachin.gupta@intelliswift.co.in"
    toaddr1 = "vikas.chauhan@intelliswift.co.in"
    toaddr2 =  "omkar.manjrekar@intelliswift.co.in"
    toaddr3 = "caroline.dsouza@intelliswift.co.in"
    toaddr4 = "mandar.deosthali@intelliswift.co.in"

elif x=="saturday" or x=="sunday":
    toaddr1 =  "sachin.gupta@intelliswift.co.in"
    toaddr2 = "Sameer.nagpure@intelliswift.co.in"
    toaddr3 = "ravindra.kute@intelliswift.co.in"
    toaddr4 = "mandar.deosthali@intelliswift.co.in"
    toaddr5 = "hareesh.panakanti@intelliswift.co.in"
    toaddr6 = "shopstyle@intelliswift.co.in"
    toaddr7 = "vikas.chauhan@intelliswift.co.in"
    toaddr8 = "caroline.dsouza@intelliswift.co.in"
    toaddr = "omkar.manjrekar@intelliswift.co.in"
fromaddr = "sachin.gupta@intelliswift.co.in"

# instance of MIMEMultipart 
msg = MIMEMultipart()

# storing the senders email address 
msg['From'] = fromaddr

# storing the receivers email address 
msg['To'] = toaddr

# storing the subject 
msg['Subject'] = "P0 dashboard check"

# string to store the body of the mail 
body = """Hi, 

This is an automated mail which contains the screenshots of P0 websites.

Regards,
Sachin
"""

# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain'))

sslist=os.listdir("/home/intelliswift/tools/selenium/screenshots/dashboard_check_"+dat+"_"+x+"")
sslist.sort()
for filename in sslist:

# open the file to be sent 
    attachment = open("/home/intelliswift/tools/selenium/screenshots/dashboard_check_"+dat+"_"+x+"/"+filename+"", "rb")

# instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream')

# To change the payload into encoded form 
    p.set_payload((attachment).read())

# encode into base64 
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# attach the instance 'p' to instance 'msg' 
    msg.attach(p)

# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security 
s.starttls()

# Authentication 
s.login(fromaddr, "Universe@786")

# Converts the Multipart msg into a string 
text = msg.as_string()

# sending the mail 

#s.sendmail(fromaddr, toaddr, text)
#s.sendmail(fromaddr, toaddr1, text)
if x=="daily_check":
    s.sendmail(fromaddr, toaddr, text)
    s.sendmail(fromaddr, toaddr1, text)
    s.sendmail(fromaddr, toaddr2, text)
    s.sendmail(fromaddr, toaddr3, text)
    s.sendmail(fromaddr, toaddr4, text)

if x=="saturday" or x=="sunday":
    s.sendmail(fromaddr, toaddr, text)
    s.sendmail(fromaddr, toaddr1, text)
    s.sendmail(fromaddr, toaddr2, text)
    s.sendmail(fromaddr, toaddr3, text)
    s.sendmail(fromaddr, toaddr4, text)
    s.sendmail(fromaddr, toaddr5, text)
    s.sendmail(fromaddr, toaddr6, text)
    s.sendmail(fromaddr, toaddr7, text)
    s.sendmail(fromaddr, toaddr8, text)
    s.sendmail(fromaddr, toaddr9, text)

# terminating the session 
s.quit()


'''
type env > a in terminal and search for environment variables and you will get the following values :

DISPLAY=:0
XAUTHORITY=/run/user/1000/gdm/Xauthority
PATH=/home/intelliswift/anaconda3/condabin:/home/intelliswift/.local/bin:/home/intelliswift/bin:/opt/apache-maven/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/usr/lib/jvm/java-8-oracle/bin:/usr/lib/jvm/java-8-oracle/db/bin:/usr/lib/jvm/java-8-oracle/jre/bin

Then copy paste the above lines in the crontab and finally set the crontab.

#Morning
30 07 * * * /usr/bin/python3 /home/intelliswift/tools/selenium/dcheck.py morning>> /home/intelliswift/tools/selenium/logs/d_check_morning.out 2>&1

#Afternoon
59 11 * * * /usr/bin/python3 /home/intelliswift/tools/selenium/dcheck.py afternoon>> /home/intelliswift/tools/selenium/logs/d_check_afternoon.out 2>&1

#Evening
30 15 * * * /usr/bin/python3 /home/intelliswift/tools/selenium/dcheck.py evening>> /home/intelliswift/tools/selenium/logs/d_check_evening.out 2>&1



'''

