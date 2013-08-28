#from encrypt import generate_vending_key            #uncomment to generate new private key for vending machine
#from encrypt import encrypt_url
#from encrypt import read_codes

#from read_qrcode import read
from read_qrcode import read

from encrypt_elgamal import encrypt_code

from generate_qrcode import make_qrcode
#from encrypt import declare_global_variables
#from encrypt import generate_verification_token     #uncomment to generate new verification code

#generate_vending_key()                              #uncomment to generate new private key for vending machine
#generate_verification_token()                       #uncomment to generate new verification code

url, challenge = encrypt_code('A061')

make_qrcode(url)
read(challenge)