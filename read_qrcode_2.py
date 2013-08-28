import subprocess
import time
import os
import base64

from Crypto.PublicKey import RSA 
from Crypto.Hash import MD5

from ezPyCrypto import key

def read(challenge_code):
    while True:
        os.system("cd /media/J-Drive/skripsie/vending_prog/barcodes/")
        os.system("fswebcam /media/J-Drive/skripsie/vending_prog/barcodes/test.jpg -q -r 320x240")
        time.sleep(3)
        try:
            verify_code = subprocess.check_output(["zbarimg", "/media/J-Drive/skripsie/vending_prog/barcodes/test.jpg", "-q"])
            print verify_code
            break
        except:
            print 'No code found'
        
    server_pub_key = key()
    vending_priv_key = key()
     
    key_file = open('server_key_ez.pub')
    server_pub_key_f = key_file.read()
    key_file.close()
     
    key_file = open('vending_key_ez.priv')
    vending_priv_key_f = key_file.read()
    key_file.close()
     
    server_pub_key.importKey(server_pub_key_f)
    vending_priv_key.importKey(vending_priv_key_f)
     
    verify_code = verify_code.split('[]', 2)
     
    data_block_1 = verify_code[0]
    data_block_2 = verify_code[1]
    
    data_block_1 = data_block_1.strip('QR-Code:') 
    #data_block_1 = '<StartPyCryptoMessage>\n' + data_block_1 + '\n<EndPryCryptoMessage>'
    data_block_2 = '<StartPycryptoSignature>\n' + data_block_2 + '<EndPycryptoSignature>'
    
    
    decoded_message = base64.b64decode(data_block_1)
    decrypted_message = vending_priv_key.decString(decoded_message)
    import pdb;pdb.set_trace()
    verify_test = server_pub_key.verifyString(decrypted_message, data_block_2)
    
    if decrypted_message[4:8] != challenge_code:
        print 'Invalid QR-Code. Please try again.'
        if verify_test != True:
            print 'The source of this QR-code could not be verified. Please try again.'
        #return None
    
    else:
        print "Thank you for your purchase. Enjoy your day :)"
    

    
#===============================================================================
# server_pub_key_file = open('server_key.pub')
# server_pub_key = RSA.importKey(server_pub_key_file.read())
# server_pub_key_file.close()
#     
# vending_priv_key_file = open("vending_key.priv")
# vending_priv_key = RSA.importKey(vending_priv_key_file.read())
# vending_priv_key_file.close()
#     
# encoded_data = verify_code.split("[]", 2)
# import pdb;pdb.set_trace()    
# encoded_data_block_1 = encoded_data[0].strip("QR-Code:")
# encoded_data_block_2 = encoded_data[1]
#     
# decoded_data_block_1 = base64.b64decode(encoded_data_block_1)
# decoded_data_block_2 = base64.b64decode(encoded_data_block_2)
#     
# decrypted_product_code = vending_priv_key.decrypt(decoded_data_block_1)
# decrypted_verify_code = decrypted_product_code.split('&')[1]
#  
# hash_code = MD5.new(decrypted_verify_code).digest()
# verify_test = server_pub_key.verify(hash_code, [long(decoded_data_block_2), ])
#===============================================================================

