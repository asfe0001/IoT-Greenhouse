
# mach mal kommentare bitte 
import json
import math
import time
import random
from threading import Timer
import paho.mqtt.client as mqtt


class TestObj(object):
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2


class Manager:
    def __init__(self, client: mqtt.Client):
        self.asdasd = 123
        self.x = 123
        self.client = client
        self.client.on_connect = self.on_connect
        self.topic_and_function_dictionary = {
            "testing": self.on_testing,
            "xyz": self.on_xyz,
            "sinus": self.on_sinus,
            "bodenfeuchte": self.on_bodenfeuchte

        }

    def on_bodenfeuchte(self, client, userdata, msg):
        print("on_bodenfeuchte")
        bodenfeuchte = json.loads(str(msg.payload.decode("utf-8")))
        if bodenfeuchte < 20:
            client.publish("magnetventil", 1)
            Timer(10, self.on_timeout).start()



    def on_timeout(self):
        print("on_timeout")
        client.publish("magnetventil", 0)



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
# t = Timer(1 / 5, on_timeout)
# t.start()

client.loop_forever()
# t.join()
