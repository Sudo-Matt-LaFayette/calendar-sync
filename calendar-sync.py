#!/usr/bin/env python2

from __future__ import print_function
import todoist
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from datetime import datetime
import datetime


#create empty arrays
todoistList = []
googleList = []
googleIDList = []

#initializes API and logs in
api = todoist.TodoistAPI()
api.user.login('username', 'password')

####################google calendar stuff
# Setup the Calendar API
SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('/home/pi/API/credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('calendar', 'v3', http=creds.authorize(Http()))

# Call the Calendar API
now = (datetime.datetime.utcnow()-datetime.timedelta(60)).isoformat() + 'Z'

print('Getting 60 events from google')
events_result = service.events().list(calendarId='primary', timeMin=now,
                                      maxResults=60, singleEvents=True,
                                      orderBy='startTime').execute()
events = events_result.get('items', [])

if not events:
    print('No upcoming events found.')


###add google items to list
for event in events:
    gEvent = str(event['summary'])
    gDate = str(event["start"].get('date'))
    gMerged = gEvent + " " + gDate
    print(gMerged)
    googleList.append(gMerged)
    googleIDList.append(event['id'])


################# Todoist stuff
print('*********************************')

###date parser
def todoParser (compdate):
    cutStr = compdate[12:22]
#    correctForm = ((datetime.datetime.strptime(cutStr, "%Y-%m-%d"))-datetime.timedelta(1)).strftime('%Y-%m-%d')
    return(cutStr)

def getItemDate(taskID):
    return api.items.get(taskID)['item']['due']

#add items to todoist List
for i in api.completed.get_all()['items']:
     content = str(i['content'])
#     contDate = str(i['completed_date'])
#     contDate = str(todoParser(i['date_added']))
     contDate = str(todoParser(str(api.items.get(i['id'])['item']['due'])))
#     print(api.items.get(i['id'])['item']['due'])
     entry = content + " " + contDate
     print(entry.replace(',', ''))
     todoistList.append(entry.replace(',', ''))

#prints all elements in completed todo List
for i in range(0,len(todoistList)):
         print(todoistList[i])

#compares todoist with google calendar and prints if it matches
for x in range (0,len(todoistList)):
    for y in range (0,len(googleList)):
        if todoistList[x]==googleList[y]:
#            print("I matched " + googleList[y] + ":" + googleIDList[y] + " - " + todoistList[x])
            service.events().delete(calendarId='primary', eventId=googleIDList[y]).execute()
            print("I deleted " + googleList[y] + " : " + googleIDList[y])
