#
!/usr/bin/python3
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
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

# Logic that you write
def main():
	counter=5
	while (counter):
	GPIO.output(13,1)
	time.sleep(1)
	GPIO.output(13,0)
	time.sleep(1)
	counter=counter-1
	print("write your logic here")

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
