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

def callback_method(channel):
		print("edge detected")			#displays a message if edge successfully detected

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)	#sets pin 37 as an input and enables the internal pull down resistor
GPIO.add_event_detect(31, GPIO.RISING, callback=callback_method,bouncetime=300)		#waits for pin 31 to have a rising edge
# Logic that you write
def main():

		GPIO.output(13,GPIO.input(31))		#sets pin 13 to a logic high
		sleep(0.1)			#introduces a delay


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
