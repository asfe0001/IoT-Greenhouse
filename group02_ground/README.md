# IoT-Geenhouse: Subproject Ground

## Goals of the Subproject
Measure the moisture and temperature of the soil and publish them

## List of Requirements Group02

* Plug in
* Connect data pin of temperature sensor with GPIO 21 (Pin 40)

## Overview Hardware System
* Raspberry Pi
* Temperature sensor DS18B20
* Moisture sensor Iduino
* Analog-Digital-Converter Joy-it ADS1115

## Preparation for Startup
Prepare Raspberry Pi for moisture sensor 
* Plug in ADC
* Connect ADC with moisture sensor (S -> AN0)
* Connect + with 3V3
* Connect - with GND

Prepare Raspberry Pi for temperature sensor

* Connect data pin (DAT) of temperature sensor with GPIO 21 (Pin 40)
* Connect VCC with 3V3
* Connect GND with GND

* Activate 1-wire protocol
```
sudo modprobe w-1gpio
sudo modprobe w1-therm
```
* Update config
```
sudo nano /boot/config.txt
```
* Add after the last row of config.txt
 ```
dtoverlay=w1-gpio,gpiopin=21,pullup=on
 ```
* Reboot
```
sudo reboot
```
* Switch directory
```
cd /sys/bus/w1/devices/
```
* Look for sensor (something like 28-3c01e0769645)
```
ls
```
* Change sensor name in line 3 of Temperature.py to your sensor ID
```
with open("/sys/bus/w1/devices/28-3c01e0769645/w1_slave") as tempfile:
```

Run Publisher.py

##  Developers and authors Subproject
 * Lang Maximilian
 * Reisner Nick
 * Stein Fabian
