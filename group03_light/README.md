# IoT-Geenhouse: Subproject Light

## Goals of the Subproject
-Provide Analog brightness readout for IOT-Greenhouse. Values get published on broker.
-Control a LED via inputs from Broker

## List of Requirements Group03
etc.
 * Publish random values to broker with Raspberry PI
 * Get analog readout from KY-018 to RPI via i2c Bus
 * Publish analoge readout to broker
 * Subscribe topic to control LED
 
## Overview Hardware System
* Raspberry PI 3
* KY-053 AD-Converter
* KY-018 Light Dependat Resistor (LDR)

## Preparation for Startup
* install **paho client** with ``sudo pip install paho-mqtt``
* install **adafruit i2C ADC** with ``sudo pip3 install adafruit-circuitpython-ads1x15``
## Hardware routing
![signal routing](https://user-images.githubusercontent.com/94985537/149324416-230a03ea-fdb1-4d14-bd33-b21e2e305ccc.png)

##  Developers and authors Subproject
 * Nils Temmesfeld
 * Jakob Mahn
 * Nils Rottmann
 ## Shopping List
 *LED RING
 *https://www.reichelt.de/entwicklerboards-neopixel-ring-mit-12-ws2812rgb-leds-debo-led-np12-p235468.html?&trstct=pos_0&nbc=1
 
 *LIGHT SENSOR
 *https://www.reichelt.de/entwicklerboards-digitaler-lichtsensor-bh1750-debo-bh-1750-p224217.html?&trstct=pos_6&nbc=1

 *Raspberry pi*
