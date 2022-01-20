import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

def getMoisture():
        try:
                # Create the I2C bus
                i2c = busio.I2C(board.SCL, board.SDA)

                # Create the ADC object using the I2C bus
                ads = ADS.ADS1015(i2c)

                # Create single-ended input on channel 0
                chan = AnalogIn(ads, ADS.P0)

                moisture_min = 144                      # 0.018 V = 144 : 0%
                moisture_max = 13584                    # 1.7V = 13584 : 100%

                moisture_raw = chan.value

                if moisture_raw <= moisture_min:
                        moisture_raw = moisture_min
                elif moisture_raw >= moisture_max:
                        moisture_raw = moisture_max
                moisture_percent = (100/(moisture_max - moisture_min)) * (moisture_raw - moisture_min)

                return moisture_percent
        except:
                return float('nan')
