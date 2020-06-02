from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notify(title,message):
    notification.notify(
        title=title,
        message = message,
        app_icon = "virus.ico",
        timeout = 10
    )

def getData(url):
    r = requests.get(url)
    return r.text


myhtmldata = getData("https://www.mohfw.gov.in/")
soup = BeautifulSoup(myhtmldata,'html.parser')
#print(soup.prettify())
myDataStr=""

for tr in soup.find_all('tbody')[0].find_all('tr'):
    myDataStr+=tr.get_text()
myDataStr = myDataStr[1:]
itemList = myDataStr.split("\n\n")
#print(itemList)

print("########  Welcome To Indian Corona Virus Notification system (By Dragonman164) ########")
print("######## Get Real Time Notification of all Indian States and Union Territories ########")
statesdict = {}
stateslist=[]
nameofstate = ""
noofStates = 0
try:
    noofStates = int(input("Enter number of States of which you want to be notified : "))
except:
    print("Please enter an Integer Only!!! Exiting......")
    exit(1)

for i in range(0,noofStates):
    nameofstate=input("Enter Name of The " + str(i+1) + " State: ")
    statesdict[nameofstate]=0
    stateslist.append(nameofstate)

for item in itemList[0:35]:
    datalist = item.split('\n')
    if datalist[1] in stateslist:
        #print(datalist)
        statesdict[datalist[1]] = 1
        nTitle = 'Cases of Covid-19'
        nText  = f"State : {datalist[1]}\nActive Cases : {datalist[2]}\nCured/Discharged/Migrated : {datalist[3]}\nDeaths : {datalist[4]} Total Cases : {datalist[5]}"
        notify(nTitle,nText)
        time.sleep(5)
        statesdict[datalist[1]]=1

for key in statesdict:
    if statesdict[key] == 0:
        notify("State Not Found",key +" State is not found in our Database. Please Type Correctly!!! \n ")


