from pickle import TRUE
import wiotp.sdk.device
import time
import os
import datetime
import random

myConfig = {"identity" : {"orgId" : "ka1ghd", "typeId" : "NodeMCU", "deviceId" : "250402"}, "auth" : {"token" : "9487936557"}}

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform : %s" % cmd.data['command'])
    m = cmd.data['command']

    if(m == 'motoron'):
        print("Motor is switched on")

    elif(m == "motoroff"):
        print("Motor is switched off")

    print(" ")

while TRUE:
    soil = random.randint(0, 100)
    temp = random.randint(-20, 125)
    hum = random.randint(0, 100)

    myData = {'soil_moisture' : soil, 'temperature' : temp, 'humidity' : hum}

    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)

    print("Published data successfully : ", myData)

    time.sleep(2)

    client.commandCallback = myCommandCallback

client.disconnect()