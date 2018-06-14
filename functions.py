#references: https://stackoverflow.com/questions/19229190/convert-12-hour-into-24-hour-times
import os
import json
from datetime import datetime

def writingToFile(point, road, direction):
    directory = './out'
    newFile = direction + '_' + road + '_' + point
    f = open(newFile,"w")
    f.write("5 Minutes,Lane 1 Flow (Veh/5 Minutes),# Lane Points,% Observed")
    for file in os.listdir(directory):
        if file.endswith(".json"):
            write = ""
            fileName = os.path.join(file)
            write = readingFile(directory,fileName,point,road,direction)
            if(write != None):
                f.write(write)
    f.close()



def readingFile(directory,fileName,point,road,direction):
    file =  open(directory+'/'+fileName, "r")
    date = getDate(fileName)
    if(os.stat(directory+'/'+fileName).st_size != 0):
        with open(directory+'/'+fileName) as f:
            data = json.load(f)
            for x in data:
                if x["line"] == road + ' ' + point:
                    status = getTraffic(x[direction]["status"])
                    time = getTime(x[direction]["time_updated"])
                    print(str(date + ' ' + time + ',' + status + ",1,100"))
                    return str(date + ' ' + time + ',' + status + ",1,100" + '\n')



def getDate(fileName):
    #04/01/2016
    dateYear = fileName.split('-')[2][:4]
    dateMonth = fileName.split('-')[2][4:6]
    dateDay = fileName.split('-')[2][6:8]
    date = dateDay + '/' + dateMonth + '/' + dateYear
    return date

def getTraffic(status):
    if status == "light":
        return '25'
    elif status == "mod":
        return '50'
    elif status == "heavy":
        return '75'
    else:
        return '404'

def getTime(time):
    inTime = datetime.strptime(time, "%I:%M %p")
    outTime = datetime.strftime(inTime, "%H:%M")
    return outTime

# writingToFile(point, road, direction)
