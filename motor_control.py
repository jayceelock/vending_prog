"""
This is the motor_control module of the vending machine. It controls the motors 
using the GPIO from the Raspberry Pi.
"""

import RPi.GPIO as GPIO
import time

def motor_switch(motor):
    print('Activating motor' + str(motor))
    
    #Set the GPIO's to output mode
    GPIO.setmode(GPIO.BOARD)
  
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
      
    if motor == 1:
        GPIO.output(12, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(12, GPIO.LOW)
          
    if motor == 2:
        GPIO.output(16, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(16, GPIO.LOW)

    
    