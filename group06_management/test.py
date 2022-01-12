
# mach mal kommentare bitte  und du darfst es gerne umbauen 

import json
import math
import time
import random
from threading import Timer
import paho.mqtt.client as mqtt

Topics = [("Greenhouse/KnowledgeBase",0),("Greenhouse/Ground/Bodenfeuchte",0),("Greenhouse/Licht/Helligkeit",0)]




class TestObj(object):
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2


class Manager:
    bodenfeuchte_max = 0
    bodenfeuchte_min = 0
    helligkeit_min = 0
    helligkeit_max = 0
    co2_max = 0
    co2_min = 0

    def __init__(self, client: mqtt.Client):
        self.asdasd = 123
        self.x = 123
        self.x = 123
        #self.bodenfeuchte_soll = 0
        #self.helligkeit_soll = 0
        self.client = client
        self.client.on_connect = self.on_connect
        self.topic_and_function_dictionary = {
        	"testing": self.on_testing,
            "xyz": self.on_xyz,
            "sinus": self.on_sinus,
            "bodenfeuchte": self.on_bodenfeuchte,
            "Greenhouse/KnowledgeBase": self.on_knowlegebase,
            "Greenhouse/Ground/Bodenfeuchte": self.on_bodenfeuchte,
            "Greenhouse/Licht/Helligkeit": self.on_helligkeit,
        }

    def on_bodenfeuchte(self, client, userdata, msg):
        print("on_bodenfeuchte")
        bodenfeuchte = json.loads(str(msg.payload.decode("utf-8")))
        if bodenfeuchte =< bodenfeuchte_min:
            client.publish("magnetventil", 1)
            Timer(10, self.on_timeout).start()
        elif bodenfeuchte >= bodenfeuchte_max:
            client.publish("magnetventil", 0)
            Timer(10, self.on_timeout).start()
        #else:
        #   client.publish("magnetventil", 0)
        #  Timer(10, self.on_timeout).start()

    def on_helligkeit(self, client, userdata, msg):
        print("on_helligkeit)
        helligkeit = json.loads(str(msg.payload.decode("utf-8")))
        if helligkeit =< helligkeit_min:
            client.publish("lichtquelle", 1)
            Timer(10, self.on_timeout).start()
        if helligkeit >= helligkeit_max:
            client.publish("lichtquelle", 0)
            Timer(10, self.on_timeout).start()

    
    def on_co2(self, client, userdata, msg):
        print("on_co2")
        co2 = json.loads(str(msg.payload.decode("utf-8")))
        if co2 =< co2_min:
            client.publish("lüften", 1)
            Timer(10, self.on_timeout).start()
        if co2 >= co2_max:
            client.publish("lüften", 0)
            Timer(10, self.on_timeout).start()

    def on_timeout(self):
        print("on_timeout")
        client.publish("magnetventil", 0)

    def on_knowlegebase(selfe):
        print('Knowlege')
        knowlege = json.loads(str(msg.payload.decode("utf-8")))
        bodenfeuchte_max = knowlege.get("Bodenfeuchte").get("Max")
        bodenfeuchte_min = knowlege.get("Bodenfeuchte").get("Min")
        helligkeit_max = knowlege.get("Helligkeit").get("Max")
        helligkeit_min = knowlege.get("Helligkeit").get("Min")
        co2_max = knowlege.get("CO2").get("Min")
        co2_min = knowlege.get("CO2").get("Min")


    def on_connect(self, client, userdata, flags, rc):
        for topic, function in self.topic_and_function_dictionary.items():
            client.subscribe(topic)
            client.message_callback_add(topic, function)

    def on_testing(self, client, userdata, msg):
        print("on_testing")
        # payload = json.loads(str(msg.payload.decode("utf-8")))
        payload = json.loads(msg.payload)
        asd = TestObj(**payload)

        print(f'{asd.var1}, {asd.var2}')

    def on_xyz(self, client, userdata, msg):
        print("on_xyz")
        payload = json.loads(str(msg.payload.decode("utf-8")))

        self.x -= 1
        print(self.x)

    def on_sinus(self, client, userdata, msg):
        print("on_sinus")
        testobj = TestObj(random.random(), random.random())
        client.publish("testobj", json.dumps(testobj.__dict__))


def on_timeout():
    # print(datetime.today().strftime('%Y-%m-%d-%H:%M:%S.%f')[:-3])
    Timer(1 / 10, on_timeout).start()
    client.publish(f"{random.getrandbits(128)}", random.getrandbits(128))
    client.publish("sinus", math.sin((time.time() * 6) % (2 * math.pi)))
    client.publish("sinus2", math.sin(time.time() * 6))


client = mqtt.Client()
manager = Manager(client)
broker_address = "cf8da10a-0d29-41a9-9c59-beb2051be054.ka.bw-cloud-instance.org"
client.connect(broker_address, 1883, 60)
client.subscribe(Topics)
#client.message_callback_add(Topics[1][0], on_knowlegebase)  #attach on_message function to a callback function
#client.message_callback_add(Topics[2][0], on_bodenfeuchte)  #attach on_message function to a callback function
#client.message_callback_add(Topics[3][0], on_helligkeit) 



# t = Timer(1 / 5, on_timeout)
# t.start()

client.loop_forever()
# t.join()
