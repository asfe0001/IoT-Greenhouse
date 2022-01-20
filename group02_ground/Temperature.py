def getTemperature():
    try:
        with open("/sys/bus/w1/devices/28-3c01e0769645/w1_slave") as tempfile:
            inhalt = tempfile.read()
            tempfile.close()
        tempdata = inhalt.split("\n")[1].split(" ")[9]
        temperatur = float(tempdata[2:])/1000
        return temperatur
    except:
        return float('nan')
