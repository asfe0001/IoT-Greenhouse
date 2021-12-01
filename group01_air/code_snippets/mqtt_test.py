import paho.mqtt.client as mqtt
import json
 
username = "ubuntu"
password = "ubuntu"
adress = "cf8da10a-0d29-41a9-9c59-beb2051be054.ka.bw-cloud-instance.org"

message = json.dumps({"testvalue" : "99"})

client = mqtt.Client()
client.username_pw_set(username, password)
client.connect(adress, 1883, 60)
 
client.publish("Greenhouse/Air/Nachrichtanmarvin", message)
client.disconnect()
