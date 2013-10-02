import qrcode
import os

def make_qrcode(data):
    qr = qrcode.QRCode(
                       version = None,
                       box_size = 6,
                       )
    
    qr.add_data(data)
    qr.make(fit = True)
    
    qrcoded_image = qr.make_image()
    
    path = os.getcwd()

    qrcoded_image.save(path + "/qrcode.png")
    #qrcoded_image.save("/media/jaycee/J-Drive/skripsie/vending_prog/qrcode.png")
