"""
This is the QR Code generation scipt. It uses the python-qrcode module to 
embed the URL into a QR Code.
"""

import qrcode
import os

#Embed the data into a QR Code
def make_qrcode(data):
    qr = qrcode.QRCode(
                       version = None,
                       box_size = 6,
                       )
    
    qr.add_data(data)
    qr.make(fit = True)
    
    qrcoded_image = qr.make_image()
    
    path = os.getcwd()
    
    #Save the image to the disk
    qrcoded_image.save(path + "/qrcode.png")