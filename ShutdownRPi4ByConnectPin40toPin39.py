import RPi.GPIO as GPIO
import os
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN,pull_up_down=GPIO.PUD_UP)

try:
    while True:
        if GPIO.input(21) == False:
            sleep(1)
            if GPIO.input(21) == False:
                os.system("sudo shutdown -h now")
                break
        sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()