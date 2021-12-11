# Ground
import paho.mqtt.client as mqtt
import time 
import json 
from random import randrange, uniform
from Temperature import *
from Humidity import *

"""Setup"""
# Broker
mqttBroker = "cf8da10a-0d29-41a9-9c59-beb2051be054.ka.bw-cloud-instance.org"
client = mqtt.Client("Ground")
client.connect(mqttBroker)

# Temperature sensor
setupTemperature()

# Humidity sensor
setupHumidity()

"""Publish loop"""
try:
    while True:
        # Get sensor values
        Bodentemperatur = getTemperature()
        Bodenfeuchte = getHumidity()
       
        print("update") 
        
        # Update JSON values
        publisher_temperature = {
            "Bodentemperatur": Bodentemperatur
            }
        publisher_humidity = {
            "Bodenfeuchte": Bodenfeuchte
            }

        # Prepare Publisher
        publisher_json1 = json.dumps(publisher_temperature)
        publisher_json2 = json.dumps(publisher_humidity) 
    
        # Publish JSON
        client.publish("IoTGreenhouse/Ground/Temperature",publisher_json1)
        client.publish("IoTGreenhouse/Ground/Humidity",publisher_json2)

        #print("Bodentemperatur:",publisher_json1)
        #print("Bodenfeuchte:",publisher_json2)
        time.sleep(1)
       
except KeyboardInterrupt:
    print("Process interrupted by a keyboard input")