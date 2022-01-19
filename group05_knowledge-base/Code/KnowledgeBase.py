import paho.mqtt.client as mqtt  # import paho-mqtt as mqtt client
import json  # import json library
import time

broker_address = "cf8da10a-0d29-41a9-9c59-beb2051be054.ka.bw-cloud-instance.org"

"""
#Topics = [("Greenhouse/Air/Outside", 0), ("Greenhouse/Air/Inside", 0)]
#subscriber_dict_air_outside = {}
#subscriber_dict_air_inside = {}


def callback_air_outside(client, userdata, message):  # callback function to receive every published message#   global subscriber_dict_air_outside
    subscriber_dict_air_outside = json.loads(
       str(message.payload.decode("utf-8")))  # convert received json string format into python dict
    print("message received: ", subscriber_dict_air_outside)  # print received message
    publisher_json1 = json.dumps(subscriber_dict_air_outside)
    client.publish("Greenhouse/KnowledgeBase/Wetter", publisher_json1)

def callback_air_inside(client, userdata, message):  # callback function to receive every published message
    global subscriber_dict_air_inside
    subscriber_dict_air_inside = json.loads(
        str(message.payload.decode("utf-8")))  # convert received json string format into python dict
    print("message received: ", subscriber_dict_air_inside)  # print received message
    publisher_json2 = json.dumps(subscriber_dict_air_inside)
    client.publish("Greenhouse/KnowledgeBase/Air", publisher_json2)
"""

broker_address = "cf8da10a-0d29-41a9-9c59-beb2051be054.ka.bw-cloud-instance.org"  # broker adress
client = mqtt.Client("KnowledgeBase")  # create new instance
#client.message_callback_add("Greenhouse/Air/Outside", callback_air_outside)  # attach on_message function to a callback function
#client.message_callback_add("Greenhouse/Air/Inside", callback_air_inside)  # attach on_message function to a callback function
client.connect(broker_address)  # connect to broker
client.loop_start()  # start the client loop to make it always running
#client.subscribe(Topics)  # subscribe to topic


publisher_Licht = {
            "Einheit": "%",
            "Min": 30,
            "Max": 80
        }
publisher_Bodenfeuchte = {
            "Einheit": "nutzbare Feldkapazitaet in Prozent",
            "Min": 50,
            "Max": 100
        }
publisher_CO2 = {
            "Einheit": "ppmv",
            "Min": 600,
            "Max": 1600
        }
publisher_Temperatur = {
            "Einheit": "Grad Celsius",
            "Min": 16,
            "Max": 26
        }


try:
    while True:
        print("publish")
        time.sleep(5)  # sleep or wait for 5s before continuing to the next loop

        publisher_json1 = json.dumps(publisher_Licht)
        publisher_json2 = json.dumps(publisher_Bodenfeuchte)
        publisher_json3 = json.dumps(publisher_CO2)
        publisher_json4 = json.dumps(publisher_Temperatur)

        client.publish("Greenhouse/KnowledgeBase/Light", publisher_json1)
        client.publish("Greenhouse/KnowledgeBase/Moisture",publisher_json2)
        client.publish("Greenhouse/KnowledgeBase/CO2", publisher_json3)
        client.publish("Greenhouse/KnowledgeBase/Temperature", publisher_json4)

        time.sleep(4)


except KeyboardInterrupt:
    print("process interrupted by a keyboard input")
    print("process stop")
    client.loop_stop()  # stop the client loop
    client.disconnect()  # disconnect gracefully client.disconnect()