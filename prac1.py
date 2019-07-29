#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: Junior Makgoe
Student Number: MKGPUL005
Prac: 1
Date: 26/07/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO
from time import sleep
from itertools import product

def countup(channel):
	global counter
	print("counting up")
	if (counter ==7):
		counter =0
	else:
		counter=counter+1
def countdown(channel):
	global counter
	print("counting down")
	if (counter == 0):
		counter =7
	else:
		counter=counter-1

GPIO.setmode(GPIO.BOARD)
channels = (11,13,15)

GPIO.setup(channels,GPIO.OUT)
GPIO.setup(31,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(31,GPIO.RISING, callback=countup,bouncetime=500)
GPIO.add_event_detect(12,GPIO.RISING, callback=countdown,bouncetime=500)

# Logic that you write
lst =list(product([0,1],repeat=3))
counter=0

def main():

	GPIO.output(channels,lst[counter])
	sleep(0.5)


#	if GPIO.event_detected(31):
#		GPIO.output(channels,lst[counterup])
#		sleep(5)
#		if (counterup ==7) :
#			counterup=0
#		else:
#			counterup=counterup+1
    #	else:
#		GPIO.output(channels,lst[counterdown])
#		sleep(1)
#		print(lst[counterdown])
#		if (counterdown ==0) :
#			counterdown=7
#		else:
#			counterdown=counterdown-1

# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
