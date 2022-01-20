# Ground
import paho.mqtt.client as mqtt
import time 
import json
import math
from Temperature import *
from Moisture import *

"""Setup"""
# Broker
mqttBroker = "cf8da10a-0d29-41a9-9c59-beb2051be054.ka.bw-cloud-instance.org"
client = mqtt.Client("Ground")
client.connect(mqttBroker)

"""Publish loop"""
try:
    while True:
        # Get sensor values
        Bodentemperatur = getTemperature()
        Bodenfeuchte = getMoisture()
       
        if math.isnan(Bodentemperatur):
            print("Temperature sensor failure")

        if math.isnan(Bodenfeuchte):
            print("Moisture sensor failure")
        
        # Update JSON values
        publisher_temperature = {
            "Temperature": Bodentemperatur
            }
        publisher_moisture = {
            "Moisture": Bodenfeuchte
            }

        # Prepare Publisher
        publisher_temperature = json.dumps(publisher_temperature)
        publisher_moisture = json.dumps(publisher_moisture) 
    
        # Publish JSON
        client.publish("Greenhouse/Ground/Temperature", publisher_temperature)
        client.publish("Greenhouse/Ground/Moisture", publisher_moisture)

        print("Temperature:", publisher_temperature)
        print("Moisture:", publisher_moisture)
        time.sleep(1)
       
except KeyboardInterrupt:
    print("Process interrupted by a keyboard input")
