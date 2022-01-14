# Provide Air Values for IoT-Greenhouse
# Temperature, Pressure, Humidity, CO2 of Inside and Outside


import paho.mqtt.client as mqtt
import json
import time
import requests
import bme68xConstants as cst
import bsecConstants as bsec

from bme68x import BME68X


# Function to return all sensor data as dict
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
        return data


# OpenWeather User Variables
API_key = "78bc3e43c97af0bbdb72e1150899fb66"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "Karlsruhe"
url = base_url + "appid=" + API_key + "&q=" + city_name
 
# MQTT Broker User Variables
username = "ubuntu"
password = "ubuntu"
adress = "cf8da10a-0d29-41a9-9c59-beb2051be054.ka.bw-cloud-instance.org"

# Connect to mqtt broker
client = mqtt.Client()
client.username_pw_set(username, password)
client.connect(adress, 1883, 60)

# Configure BME688 Sensor
bme = BME68X(cst.BME68X_I2C_ADDR_HIGH, 1)
bme.set_sample_rate(bsec.BSEC_SAMPLE_RATE_LP)

# Declare variables
temperatur = 0
pressure = 0
humidity = 0
co2 = 0

################################## MAIN LOOP ##################################
while (True):
    try:
        #################### Data from inside via sensor ######################

        # Get data from sensor
        bsec_data = get_data(bme)
        while bsec_data == None:
            # Try as long as no data received from sensor
            bsec_data = get_data(bme)

        # Extract relevant data from sensor
        temperature = round(bsec_data['temperature'], 1)
        pressure = round(bsec_data['raw_pressure']/100, 1)
        humidity = round(bsec_data['humidity'], 1)
        co2 = round(bsec_data['co2_equivalent'], 1)

        # Build message to publish
        message_air = json.dumps({
            "Temperature" : temperature,
            "Pressure" : pressure,
            "Humidity" : humidity,
            "CO2" : co2
            })

        # Send sensor data to mqtt broker
        client.publish("Greenhouse/Air/Inside", message_air)
        print("Sent sensor message:\t"+str(message_air))

        ################# Data from outside via weather query #################

        # Get data from OpenWeather
        server_response_json = requests.get(url).json()

        # Extract relevant data from OpenWather
        temperature = round(server_response_json["main"]["temp"]-273.15, 1)
        pressure = server_response_json["main"]["pressure"]
        humidity = server_response_json["main"]["humidity"]

        # Build message to publish
        message_weather = json.dumps({
            "Temperature" : temperature,
            "Pressure" : pressure,
            "Humidity" : humidity
            })  

        # Send weather data to mqtt broker
        client.publish("Greenhouse/Air/Outside", message_weather)
        print("Sent weather message\t", message_weather)

        # Wat period of time
        time.sleep(3)

    except KeyboardInterrupt:
        break
client.disconnect()
print("Disconnected...")
