import qrcode

def make_qrcode(data):
    qr = qrcode.QRCode(
                       version = None,
                       box_size = 4,
                       )
    
    qr.add_data(data)
    qr.make(fit = True)
    
    qrcoded_image = qr.make_image()
    
    #return qrcoded_image

    qrcoded_image.save("/media/jaycee/J-Drive/skripsie/vending_prog/qrcode.png")
    #qrcoded_image.show()
    