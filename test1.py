#!/user/bin/env python3

import time
from rpi_ws281x import *
import gpiozero import MotionSensor
import board
import argparse
import neopixel

# LED strip configuration:
LED_COUNT      = 144      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 65     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

#Initialize a strips variable, provide the GPIO Data Pin
#utilised and the amount of LED Nodes on strip and brightness (0 to 1 value)  
pixels1 = neopixel.NeoPixel(board.D18, 144, brightness=1)

n = 0

def oneledanimation(n):
    
    while n < LED_COUNT:
        pixels1[n] = (0, 0, 255)
        n = n + 1
        time.sleep(0.01)
        pixels1[n-1] = (0, 0, 0)
        
        while n == LED_COUNT:
            pixels1.fill((86,86,86))
            time.sleep(3)
            pixels1.fill((0, 0, 0))

pir = MotionSensor(12) #out plugged into GPIO12

while True:
    pir.wait_for_motion()
    print(Movement detected!)

    oneledanimation(n)

    pir.wait_for_no_motion()
    print("Movement is gone")
