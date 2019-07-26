#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: Junior Makgoe
Student Number: MKGPUL005
Prac: 1
Date: <26/07/2019>
"""

# import Relevant Librares
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)

# Logic that you write
def main():
		GPIO.output(13,1)		#sets pin 13 to a logic high
		sleep(1)			#introduces a one second delay
		GPIO.output(13,0)		#sets pin 13 to a logic low
		sleep(1)
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
