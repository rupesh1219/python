'''
required packages:
1. python-gnupg
2. rng-tools
'''

#generate a key
import os
import gnupg

gpg = gnupg.GPG(gnupghome = '/home/rupeshkepler/gpghome')

'''
input_data = gpg.gen_key_input(
    name_email='xyz@gmail.com',
    passphrase='xxxxx')

key = gpg.gen_key(input_data)

print(key)

#export keys

ascii_armored_public_keys = gpg.export_keys(str(key))
ascii_armored_private_keys = gpg.export_keys(str(key),True)

with open('mypublickey.asc','w') as f:
    f.write(ascii_armored_public_keys)

with open('myprivatekey.asc','w') as f:
    f.write(ascii_armored_private_keys)

#encrypt the file
open('my-unencryptedfile','w').write('learning crynptography')
with open('my-unencryptedfile','rb') as f:
    status = gpg.encrypt_file(
        f, recipients=['xyz@gmail.com'],
        output='my-encrypted.txt.gpg')
'''

# decrypt file
with open('AXAEMRKT_DEXC7213_0000001_0000113.asc','rb') as f:
    status = gpg.decrypt_file(f,passphrase = 'rupesh1219', output = 'AXAEMRKT_DEXC7213.pdf')

print('Ok:', status.ok)
print('status:', status.status)
print('status:', status.stderr)
