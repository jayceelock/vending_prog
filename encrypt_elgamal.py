import base64
import random
import cPickle as Pickle
from Crypto.Hash import MD5
from Crypto.PublicKey import ElGamal

def encrypt_code(prod_code):
    
    server_pub_key = Pickle.load(open("server_key.pub", 'r'))
    vending_priv_key = Pickle.load(open("vending_key.priv", 'r'))
    
    rand_gen_hex = '%012x' % random.randrange(16**12)
      
    prod_string = rand_gen_hex + prod_code
    
    hash_code = MD5.new(prod_code).digest()
    
    signature = vending_priv_key.sign(hash_code, prod_code)
    
    encoded_signature = base64.urlsafe_b64encode(str(signature[0])) + '**' + base64.urlsafe_b64encode(str(signature[1]))
    
    encrypted_string = server_pub_key.encrypt(prod_string, 32)
    
    encoded_string = base64.urlsafe_b64encode(encrypted_string[0]) + '**' + base64.urlsafe_b64encode(encrypted_string[1])
    url = "http://ec2-54-213-127-119.us-west-2.compute.amazonaws.com/?code=" + encoded_string + "[]" + encoded_signature
    challenge = prod_string[4:8]
    print url
    print challenge

    return (url, challenge) 
