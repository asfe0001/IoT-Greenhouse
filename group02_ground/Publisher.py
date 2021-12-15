# Ground
import paho.mqtt.client as mqtt
import time 
import json 
from random import randrange, uniform
from Temperature import *
from Moisture import *

"""Setup"""
# Broker
mqttBroker = "cf8da10a-0d29-41a9-9c59-beb2051be054.ka.bw-cloud-instance.org"
client = mqtt.Client("Ground")
client.connect(mqttBroker)

# Temperature sensor
setupTemperature()

# Moisture sensor
setupMoisture()

"""Publish loop"""
try:
    while True:
        # Get sensor values
        Bodentemperatur = getTemperature()
        Bodenfeuchte = getMoisture()
       
        print("update") 
        
        # Update JSON values
        publisher_temperature = {
            "Bodentemperatur": Bodentemperatur
            }
        publisher_moisture = {
            "Bodenfeuchte": Bodenfeuchte
            }

        # Prepare Publisher
        publisher_temperature = json.dumps(publisher_temperature)
        publisher_moisture = json.dumps(publisher_moisture) 
    
        # Publish JSON
        client.publish("IoTGreenhouse/Ground/Temperature",publisher_temperature)
        client.publish("IoTGreenhouse/Ground/Moisture",publisher_moisture)

        #print("Bodentemperatur:",publisher_temperature)
        #print("Bodenfeuchte:",publisher_moisture)
        time.sleep(1)
       
except KeyboardInterrupt:
    print("Process interrupted by a keyboard input")