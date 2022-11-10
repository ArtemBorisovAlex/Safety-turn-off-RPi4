import RPi.GPIO as GPIO
import os
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(21,GPIO.FALLING)
os.system("sudo shutdown -h now")