import RPi.GPIO as gp
import time as t
import Adafruit_DHT as dht
# só funciona com o raspberry, devido as portas gpio
def inicializar(pin):
    sensor = dht.DHT11
    gp.setmode(gp.BCM)
    t.sleep(1)

def lerDHT(sensor, pin):

    humid,temp = dht.read_retry(sensor, pin)
    t.sleep(1)
    return humid, temp

    