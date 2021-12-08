import paho.mqtt.client as mqtt
import json
import time
 
username = "ubuntu"
password = "ubuntu"
adress = "cf8da10a-0d29-41a9-9c59-beb2051be054.ka.bw-cloud-instance.org"



client = mqtt.Client()
client.username_pw_set(username, password)
client.connect(adress, 1883, 60)
i=0
while (True):
    message = json.dumps({"testvalue" : i})
    time.sleep(1)

    value = i

    message = json.dumps({"Temperature" : value})
                            


    client.publish("Greenhouse/Air", message)
    print("Sent message:"+str(message))

    i = i+1

client.disconnect()
