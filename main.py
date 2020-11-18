from datetime import date
import currentTime as time
import eventTime
import time as timeFreeze
from mainSendMessage import sendMessage

while True:
    # Get the current time while refreshing every 5 secs:
    currentVremya = time.getCurrentTime()
    vremyaHMS = currentVremya.split(':')
    currentVremyaSecs = (int(vremyaHMS[0]) * 3600) + (int(vremyaHMS[1]) * 60) + (int(vremyaHMS[2]))
    todayDate = str(date.today()).split("-")[1]

    # Get the event time while refreshing every 5 secs, any recent updates will be added!
    eventVremya = eventTime.eventTime()
    eventDetails = eventTime.eventInfo()
    eventDai = eventTime.eventDay().split("-")[1]
    eventVremyaList = eventVremya.split(':')
    eventSecs = (int(eventVremyaList[0]) * 3600) + (int(eventVremyaList[1]) * 60) + (int(eventVremyaList[2]))

    print(eventSecs, currentVremyaSecs, currentVremyaSecs - eventSecs)

    if int(todayDate) == int(eventDai):
        if eventSecs - 60 < currentVremyaSecs < eventSecs:
            print(f"Less than a minute left for the event {eventDetails}")
            sendMessage(f"Less than a minute left for the event {eventDetails}")
            timeFreeze.sleep(61)