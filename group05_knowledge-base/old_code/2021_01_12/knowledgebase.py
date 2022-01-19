#!/usr/bin/python
# coding=utf-8
# Provide constant values for initialization
# could advanced to save data at runtime.

import math
import paho.mqtt.client as mqtt
import json
import time

# MQTT Broker User Variables0
username = "ubuntu"
password = "ubuntu"
adress = "cf8da10a-0d29-41a9-9c59-beb2051be054.ka.bw-cloud-instance.org"
client = mqtt.Client()
client.username_pw_set(username, password)
client.connect(adress, 1883, 60)


# Build Message for CO2
message_CO2 = json.dumps(
{
    "Plant": "ganja",
    "Unit":     "ppm",
    "Min":        100,
    "Max":        400
}
) 

# Build Message for Light
message_Light = json.dumps(
{
    "Plant": "ganja",
    "Unit":     "Lux",
    "Min":        500,
    "Max":       3000
}
)

# Build Message for Moisture
message_moisture = json.dumps(
{
    "Plant": "ganja",
    "Unit":       "%",
    "Min":         50,
    "Max":        100
}
)

# Build Message for Temperature
message_temperature = json.dumps(
{
    "Plant": "ganja",
    "Unit":      "°C",
    "Min":         25,
    "Max":         50
}
)



while (True):

    # Send Messages
    client.publish("Greenhouse/KnowledgeBase2/CO2", message_CO2)
    client.publish("Greenhouse/KnowledgeBase2/Light", message_Light)
    client.publish("Greenhouse/KnowledgeBase2/Moisture", message_moisture)
    client.publish("Greenhouse/KnowledgeBase2/temperature", message_temperature)

    time.sleep(5)
