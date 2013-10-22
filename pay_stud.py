"""
This is the pay_stud module. It allows the vending machine to process payments 
made via RFID card using the libnfc library.
"""

import subprocess

def process_card():
    #Read the RFID card's UID using the nfc-poll module from libfc
    process = subprocess.Popen('nfc-poll', stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    
    out, err = process.communicate()
    
    #Process the output and make it pretty
    out = out.split('\n')
    
    uid_line = out[5]
    
    uid = uid_line.split(':')[1]
    
    uid = uid.replace(" ", '')
    
    return uid