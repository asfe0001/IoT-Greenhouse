import json
import paho.mqtt.client as mqtt


class Knowledge(object):
    # Knowledge muss diesem Json-Format entsprechen
    # {
    #   "bodenfeuchte_max" : 10,
    #   "bodenfeuchte_min" : 0,
    #   "helligkeit_max": 10,
    #   "helligkeit_min": 0,
    #   "co2_max": 10,
    #   "co2_min": 0
    # }
    def __init__(self, bodenfeuchte_max=100, bodenfeuchte_min=0, helligkeit_max=100, helligkeit_min=0, co2_max=100,
                 co2_min=0):
        self.bodenfeuchte_max = bodenfeuchte_max
        self.bodenfeuchte_min = bodenfeuchte_min
        self.helligkeit_max = helligkeit_max
        self.helligkeit_min = helligkeit_min
        self.co2_max = co2_max
        self.co2_min = co2_min


class Manager:
    bodenfeuchte = 0
    helligkeit = 0
    co2 = 0
    knowledge = Knowledge()
    def __init__(self):
        # Erzeuge eine Instanz von dem Knowledge-Objekt, welches oben beschrieben ist
        # self.knowledge = Knowledge()
        # self.bodenfeuchte = 0
        # self.helligkeit = 0
        # self.co2 = 0
        client.on_connect = self.on_connect
        # Dieses Tuple enthält die Namen der Topics und die entsprechenden Event-Handler
        self.topic_and_function_dictionary = {
            "Greenhouse/KnowledgeBase": self.on_knowledgebase,
            "Greenhouse/Ground/Bodenfeuchte": self.on_bodenfeuchte,
            "Greenhouse/Licht/Helligkeit": self.on_helligkeit,
        }

    def initial_setup(self):
        # Wird bei der Initialiserung ausgeführt oder wenn sich die Knowledge ändert
        self.set_bodenfeuchte(self.bodenfeuchte)
        self.set_helligkeit(self.helligkeit)
        self.set_co2(self.co2)


    def on_bodenfeuchte(self, client, userdata, msg):
        print("on_bodenfeuchte")
        self.set_bodenfeuchte(json.loads(str(msg.payload.decode("utf-8"))))

    def set_bodenfeuchte(self, bodenfeuchte):
        # Wenn bodenfeuchte in Nähe von bodenfeuchte_min kommt (120%) --> dann magnetventil an
        # Magnetventil ausschalten, wenn Mittelwert erreicht wird
        self.bodenfeuchte = bodenfeuchte
        if bodenfeuchte <= 1.2 * self.knowledge.bodenfeuchte_min:
            client.publish("magnetventil", 1)
        elif bodenfeuchte >= (self.knowledge.bodenfeuchte_min + self.knowledge.bodenfeuchte_max) / 2:
            client.publish("magnetventil", 0)

    def on_helligkeit(self, client, userdata, msg):
        print("on_helligkeit")
        self.set_helligkeit(json.loads(str(msg.payload.decode("utf-8"))))

    def set_helligkeit(self, helligkeit):
        # Wenn helligkeit in Nähe von helligkeit_min kommt (120%) --> dann Lichtquelle an
        # Lichtquelle ausschalten, wenn Mittelwert erreicht wird
        self.helligkeit = helligkeit
        if helligkeit <= 1.2 * self.knowledge.helligkeit_min:
            client.publish("lichtquelle", 1)
        elif helligkeit >= (self.knowledge.helligkeit_min + self.knowledge.helligkeit_max) / 2:
            client.publish("lichtquelle", 0)

    def on_co2(self, client, userdata, msg):
        print("on_co2")
        self.set_co2(json.loads(str(msg.payload.decode("utf-8"))))

    def set_co2(self, co2):
        # co2-Wert steigt bei geschlossenem Fenster --> lüften, wenn co2-Wert in Nähe co2_max kommt (80%) erreicht wird
        # Mit Lüften aufhören, wenn Mittelwert erreicht wird
        self.co2 = co2
        if co2 <= (self.knowledge.co2_min + self.knowledge.co2_max) / 2:
            client.publish("lüften", 0)
        elif co2 >= 0.8 * self.knowledge.co2_max:
            client.publish("lüften", 1)

    def on_knowledgebase(self, client, userdata, msg):
        print('on_knowledgebase')
        payload = json.loads(msg.payload)
        self.knowledge = Knowledge(**payload)
        self.print_knowledge()
        self.initial_setup()


    def print_knowledge(self):
        print(
            f'bodenfeuchte_max={self.knowledge.bodenfeuchte_max}, bodenfeuchte_min={self.knowledge.bodenfeuchte_min}, helligkeit_max={self.knowledge.helligkeit_max}, helligkeit_min={self.knowledge.helligkeit_min}, co2_max={self.knowledge.co2_max}, co2_min={self.knowledge.co2_min}')

    def on_connect(self, client, userdata, flags, rc):
        # on_connect wird aufgerufen, sobald die Verbindung zum Broker hergestellt wurde
        print("on_connect")
        for topic, function in self.topic_and_function_dictionary.items():
            # client subscribed dann zu den Topics, die oben festgelegt wurden
            client.subscribe(topic)
            # ... und registriert die callbacks/event-handler-funktionen
            client.message_callback_add(topic, function)
        self.initial_setup()


client = mqtt.Client()
manager = Manager()
broker_address = "cf8da10a-0d29-41a9-9c59-beb2051be054.ka.bw-cloud-instance.org"
client.connect(broker_address, 1883, 60)
client.loop_forever()
