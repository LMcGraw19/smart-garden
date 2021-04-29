# credit to https://stackoverflow.com/questions/54292179/saving-mqtt-data-from-subscribe-topic-on-a-text-file Yugandhar Chaudhari

import paho.mqtt.client as mqttClient
import time

def on_connect(client, userdata, flags, rc):

    if rc == 0:

        print("Connected to broker")

        global Connected                #Use global variable
        Connected = True                #Signal connection

    else:

        print("Connection failed")

def on_message(client, userdata, message):
    with open('/home/test.txt','a+') as f: # Insert write path here
         sentcontents=str(message.payload).strip('[b\'\']')
         f.write(message.payload)

Connected = False   #global variable for the state of the connection

broker_address= ""  #Broker address
port = 8883                         #Broker port
user = ""                    #Connection username
password = ""            #Connection password

client = mqttClient.Client("self")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback
client.connect(broker_address,port,60) #connect
client.subscribe("some/topic") #Topic File path here
client.loop_forever() #then keep listening forever
