from tkinter import*
from tkinter.ttk import*
import paho.mqtt.client as mqtt #import paho-mqtt as mqtt client
import json #import json library
import time

broker_address="cf8da10a-0d29-41a9-9c59-beb2051be054.ka.bw-cloud-instance.org"
# root = Tk()
# root.wm_title("Gewächshaus GUI")
# root.config(background = "#FFFFFF")

Topics = [("Greenhouse/Air/Inside",0),("Greenhouse/Air/Outside",0)]#,("Greenhouse/Light/Brightness",0),("Greenhouse/Knowledge/Wetter",0)]#,("Greenhouse/Ground",0),("Greenhouse/Air",0)]
subscriber_dict_knowledge = {}
subscriber_dict_light = {}
#subscriber_dict_water = {}
#subscriber_dict_ground = {}
subscriber_dict_air = {}


def callback_air_inside(client, userdata, message):  #callback function to receive every published message
    global subscriber_dict_air
    global Temperature
    global Pressure
    subscriber_dict_air = json.loads(str(message.payload.decode("utf-8"))) #convert received json string format into python dict
    #print("message received: ", subscriber_dict_air) #print received message
    Temperature=subscriber_dict_air["Temperature"]
    print("Temperature:", Temperature)
    Pressure=subscriber_dict_air["Pressure"]
    print("Pressure: ", Pressure)
    
def callback_air_outside(client, userdata, message):  #callback function to receive every published message
    global subscriber_dict_air
    global Temperature
    global Pressure
    subscriber_dict_air = json.loads(str(message.payload.decode("utf-8"))) #convert received json string format into python dict
    #print("message received: ", subscriber_dict_air) #print received message
    Temperature=subscriber_dict_air["Temperature"]
    print("Temperature Outside:", Temperature)
    Pressure=subscriber_dict_air["Pressure"]
    print("Pressure Outside: ", Pressure)
    
broker_address="cf8da10a-0d29-41a9-9c59-beb2051be054.ka.bw-cloud-instance.org" #broker adress
client = mqtt.Client("Manager_Boss") #create new instance
client.message_callback_add("Greenhouse/Air/Inside", callback_air_inside)  #attach on_message function to a callback function
client.message_callback_add("Greenhouse/Air/Outside", callback_air_outside)  #attach on_message function to a callback function
client.connect(broker_address) #connect to broker
client.loop_start() #start the client loop to make it always running
client.subscribe(Topics) #subscribe to topic

# luftFrame = Frame(root, width= 310, height = 125)
# luftFrame.grid(row=0, column=0, padx=10, pady=3)
# luftLabel = Label(luftFrame, text="Luftzustand")
# luftLabel.grid(row=0, column=0, padx=10, pady=3)
# 
# bodenFrame = Frame(root, width= 310, height = 125)
# bodenFrame.grid(row=1, column=0, padx=10, pady=3)
# bodenLabel = Label(bodenFrame, text="Bodenzustand")
# bodenLabel.grid(row=0, column=0, padx=10, pady=3)
# 
# wasserFrame = Frame(root, width= 310, height = 125)
# wasserFrame.grid(row=2, column=0, padx=10, pady=3)
# wasserLabel = Label(wasserFrame, text="Wasserzustand")
# wasserLabel.grid(row=0, column=0, padx=10, pady=3)
# 
# lichtFrame = Frame(root, width= 310, height = 125)
# lichtFrame.grid(row=3, column=0, padx=10, pady=3)
# lichtLabel = Label(lichtFrame, text="Lichtzustand")
# lichtLabel.grid(row=0, column=0, padx=10, pady=3)
# 
# luftReglerFrame = Frame(root, width= 310, height = 125)
# luftReglerFrame.grid(row=0, column=1, padx=10, pady=3)
# 
# bodenReglerFrame = Frame(root, width= 310, height = 125)
# bodenReglerFrame.grid(row=1, column=1, padx=10, pady=3)
# 
# wasserReglerFrame = Frame(root, width= 310, height = 125)
# wasserReglerFrame.grid(row=2, column=1, padx=10, pady=3)
# 
# lichtReglerFrame = Frame(root, width= 310, height = 125)
# lichtReglerFrame.grid(row=3, column=1, padx=10, pady=3)
# 
# luftEinheitFrame = Frame(root, width= 310, height = 125)
# luftEinheitFrame.grid(row=0, column=2, padx=10, pady=3)
# 
# bodenEinheitFrame = Frame(root, width= 310, height = 125)
# bodenEinheitFrame.grid(row=1, column=2, padx=10, pady=3)
# 
# wasserEinheitFrame = Frame(root, width= 310, height = 125)
# wasserEinheitFrame.grid(row=2, column=2, padx=10, pady=3)
# 
# lichtEinheitFrame = Frame(root, width= 310, height = 125)
# lichtEinheitFrame.grid(row=3, column=2, padx=10, pady=3)

#root.mainloop()
