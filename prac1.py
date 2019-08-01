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
import RPi.GPIO as GPIO				#imports python libraries
from time import sleep				#import sleep module to be used for delays
from itertools import product			#imoprts itertools module product

def countup(channel):				#defines a function that will increment a counter value
	global counter				 #when interrupt is detected
	print("counting up")
	if (counter ==7):			#checks if the final value in the array has been reached,
		counter =0			 #if so the counter variable is reset to zero
	else:
		counter=counter+1
def countdown(channel):				#defines a function that will decrement a counter value
	global counter
	print("counting down")
	if (counter == 0):
		counter =7			#checks if the first value in the array has been reached,
	else:					 #if so, it goes back to the highest number in array
		counter=counter-1

GPIO.setmode(GPIO.BOARD)			#indicates that pin numbers are used
channels = (11,13,15)				#channels to be initialized

GPIO.setup(channels,GPIO.OUT)			#sets channels to output pins

#sets pin 31 as an input and initalizes the pull down resistors
GPIO.setup(31,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

#creates interrupt when switch is pressed and calls functions
GPIO.add_event_detect(31,GPIO.RISING, callback=countup,bouncetime=500)
GPIO.add_event_detect(12,GPIO.RISING, callback=countdown,bouncetime=500)

# generates an array of binary values from [0,0,0] to [1,1,1]
#defines a counter variable
lst =list(product([0,1],repeat=3))
counter=0

def main():

	#sends binary array values to be output on the LEDs and delays for 0.5 seconds
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
