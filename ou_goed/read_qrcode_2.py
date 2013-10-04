#!/usr/bin/python
from Crypto.Hash import MD5
from sys import argv
import base64
import cPickle as Pickle
import zbar

#while 1:
def read(challenge_code):
    # create a Processor
    proc = zbar.Processor()

    # configure the Processor
    proc.parse_config('enable')

    # initialize the Processor
    device = '/dev/video0'
    if len(argv) > 1:
        device = argv[1]
    proc.init(device)
    
    # enable the preview window
    proc.visible = True

    # read at least one barcode (or until window closed)
    proc.process_one()
    
    # hide the preview window
    proc.visible = False
    
    # extract results
    for symbol in proc.results:
        # do something useful with results
        verify_code = symbol.data
     
    server_pub_key = Pickle.load(open("server_key.pub", 'r'))
     
    vending_priv_key = Pickle.load(open("vending_key.priv", 'r'))
     
    verify_code = verify_code.split('[]', 2)
    encoded_string = verify_code[0].split('**', 2)
    encoded_signature = verify_code[1].split('**', 2)
     
    encrypted_string = (base64.b64decode(encoded_string[0]), base64.b64decode(encoded_string[1]))
    signature = (long(base64.b64decode(encoded_signature[0])), long(base64.b64decode(encoded_signature[1])))
    import pdb; pdb.set_trace();    
     
    
    #decoded_message = base64.b64decode(data_block_1)
    #decoded_signature = base64.b64decode(data_block_2)
    
    decrypted_message = vending_priv_key.decrypt(encrypted_string)
    #encrypted_string = encrypted_string.strip('QR-Code:')
    hash_code = MD5.new(decrypted_message[4:8]).digest()
    
    verify_test = server_pub_key.verify(hash_code, signature)
    
    if decrypted_message[4:8] != challenge_code:
        print 'Invalid QR-Code. Please try again.'
        if verify_test != True:
            print 'The source of this QR-code could not be verified. Please try again.'
        #return None
    
    else:
        print "Thank you for your purchase. Enjoy your day :)"
    #break