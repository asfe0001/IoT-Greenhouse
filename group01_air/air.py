# Provide Air Values for IoT-Greenhouse
# Temperature, Pressure, Humidity, CO2


import paho.mqtt.client as mqtt
import json
import time
import requests
from bme68x import BME68X
import bme68xConstants as cst
import bsecConstants as bsec

# OpenWeather User Variables
API_key = "78bc3e43c97af0bbdb72e1150899fb66"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "Karlsruhe"
url = base_url + "appid=" + API_key + "&q=" + city_name
 
# MQTT Broker User Variables
username = "ubuntu"
password = "ubuntu"
adress = "cf8da10a-0d29-41a9-9c59-beb2051be054.ka.bw-cloud-instance.org"

client = mqtt.Client()
client.username_pw_set(username, password)
client.connect(adress, 1883, 60)

# Configure BME688 Sensor

bme = BME68X(cst.BME68X_I2C_ADDR_HIGH, 1)
bme.set_sample_rate(bsec.BSEC_SAMPLE_RATE_LP)


def get_data(sensor):
    data = {}
    try:
        data = sensor.get_bsec_data()
    except Exception as e:
        print(e)
        return None
    if data == None or data == {}:
        time.sleep(0.1)
        return None
    else:
        time.sleep(3)
        return data



i=0 # dummy value

temperatur = 0
pressure = 0
humidity = 0
co2 = 0


while (True):
    try:
        time.sleep(1)
        # Get values from sensor
        bsec_data = get_data(bme)
        while bsec_data == None:
            bsec_data = get_data(bme)
        temperature = round(bsec_data['temperature'], 1)
        pressure = round(bsec_data['raw_pressure']/100, 1)
        humidity = round(bsec_data['humidity'], 1)
        co2 = bsec_data['co2_equivalent']

        # Build messages to publish
        message_air = json.dumps({
            "Temperature" : temperature,
            "Pressure" : pressure,
            "Humidity" : humidity,
            "CO2" : co2
            })

        server_response_json = requests.get(url).json()
        # Get values from OpenWeather
        temperature = round(server_response_json["main"]["temp"]-273.15, 1)
        pressure = server_response_json["main"]["pressure"]
        humidity = server_response_json["main"]["humidity"]

        # Build messages to publish
        message_weather = json.dumps({
            "Temperature" : temperature,
            "Pressure" : pressure,
            "Humidity" : humidity
            })  

        
        
        client.publish("Greenhouse/Air/Inside", message_air)
        print("Sent message:"+str(message_air))

        client.publish("Greenhouse/Air/Outside", message_weather)
        print("Sent weather message", message_weather)

        i = i+1

    except KeyboardInterrupt:
        break
client.disconnect()
print("Disconnected...")