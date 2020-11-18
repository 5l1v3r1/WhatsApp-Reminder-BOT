from datetime import datetime

def getCurrentTime():

    return datetime.now().strftime("%H:%M:%S")