from Crypto.PublicKey import RSA
from Crypto.Hash import MD5
from Crypto import Random

from random import randint

import base64

def encrypt_url(product):
    global server_public_key
    global vending_machine_verification_code
    
    product_code = product
    
    vending_priv_key = RSA.importKey(vending_machine_private_key)           #import keys
    server_pub_key = RSA.importKey(server_public_key)
    
    message = str(randint(0, 255)) + '&' + product_code
    encrypted_message = server_pub_key.encrypt(message, 32)       #encrypt product code + random int to randomise qr-code image
    
    hash_code = MD5.new(message).digest()
    
    encrypted_verification_code = vending_priv_key.sign(hash_code, '')

    data_block_1 = base64.urlsafe_b64encode(encrypted_message[0])               #ascii armour the encrypted data
    data_block_2 = base64.urlsafe_b64encode(str(encrypted_verification_code[0]))
    
    url = 'http://ec2-54-213-127-119.us-west-2.compute.amazonaws.com/?code=' + data_block_1 + '[]' + data_block_2
    
    print url
    return url
    
def read_codes():
    global vending_machine_private_key
    global vending_machine_verification_code
    global server_public_key
    
    vending_key_file = open("vending_key.priv")
    vending_machine_private_key = vending_key_file.read()
    vending_key_file.close()
    
    veri_file = open("verification.priv")
    vending_machine_verification_code = veri_file.read()
    veri_file.close()
    
    server_key_file = open("server_key.pub")
    server_public_key = server_key_file.read()
    server_key_file.close()
    
def generate_vending_key():
    random_generator = Random.new().read
    vending_machine_private_key = RSA.generate(1024, random_generator)
    
    key_file = open("vending_key.priv", "w")    
    key_file.write(vending_machine_private_key.exportKey()) 
    key_file.close()
    
    key_file = open("vending_key.pub", "w")    
    key_file.write(vending_machine_private_key.publickey().exportKey()) 
    key_file.close()
    
def generate_verification_token():
    random_bits =  ''.join(chr(randint(0, 255)) for i in range(8))
    
    verification_token_file = open("verification.priv", "w")
    verification_token_file.write(base64.b64encode(random_bits))
    verification_token_file.close()
