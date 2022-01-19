#!/usr/bin/python
# coding=utf-8
# Provide Light Values for IoT-Greenhouse

import math
import paho.mqtt.client as mqtt
import json
import time

import RPi.GPIO as GPIO

# Import BUS
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

#Message received
def on_message(client, userdata, message):
    print ("Message received: ", str(message.payload.decode("utf-8")),\
           "topic",message.topic,"retained",message.retain)
    led_status = str(message.payload.decode("utf-8"))
    if (led_status) == "1":
        GPIO.output(21, GPIO.HIGH)
    else:
        GPIO.output(21, GPIO.LOW)

#Init GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)


# MQTT Broker User Variables0
username = "ubuntu"
password = "ubuntu"
adress = "cf8da10a-0d29-41a9-9c59-beb2051be054.ka.bw-cloud-instance.org"
client = mqtt.Client()
client.username_pw_set(username, password)
client.connect(adress, 1883, 60)

#MQTT Subscribe
client.on_message = on_message
client.subscribe("Greenhouse/Light/LED_Status")
client.loop_start()

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)
voltageMax = 3.3

# Create single-ended input on channels
chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)
chan3 = AnalogIn(ads, ADS.P3)

# Define variables
led_status = "0"
uptime = 0
light = 0;

while True:
    
    #Blink
    if (uptime%2) == 1:
        GPIO.output(16, GPIO.HIGH)
    else:
        GPIO.output(16, GPIO.LOW)
    
    #Get values from Sensor via i2C Bus
    resistance = chan0.voltage / (voltageMax - chan0.voltage) * 10000
    k_resist = resistance / 1000
    
    #Print all Values
    print("Spannungswert: ", '%.2f' % chan0.voltage, "V, Widerstand: ", '%.2f' % resistance, "Î©")
    print("Widerstand K-Ohm: ", '%.2f' % k_resist)
    print("---------------------------------------------------")
    
    #Calculate Light Percentage
    if k_resist < 0.2:
        light = 100
    elif k_resist < 1.5:
        light = 90
    elif k_resist < 2:
        light = 80
    elif k_resist < 3.5:
        light = 70
    elif k_resist < 5:
        light = 60
    elif k_resist < 8:
        light = 50
    elif k_resist < 12:
        light = 40
    elif k_resist < 17:
        light = 30
    elif k_resist < 21:
        light = 20
    elif k_resist < 23.5:
        light = 10
    elif k_resist > 25:
        light = 0
    
    #Pause 1s
    time.sleep(2)

    #Send / Get information from/to Broker
    try:

        # Build messages to publish
        message_light = json.dumps({
            "Light-Percentage [%]": light,
            "Resistance [KOHM]": round(k_resist, 1),
            "Time [s]": uptime,
            })

        # Publish Message
        client.publish("Greenhouse/Light/Brightness", message_light)
        
        # Print published message
        print("Sent message:"+str(message_light))

        #Increase Uptime
        uptime = uptime+1

    except KeyboardInterrupt:
        print ("Exiting")
        client.loop_stop()
        break
GPIO.output(21, GPIO.LOW)
client.disconnect()
