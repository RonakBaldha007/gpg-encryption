"""
    python-gnupg is a Python package for encrypting and decrypting strings or files
    using GNU Privacy Guard (GnuPG or GPG).

"""

import os
import logging
import gnupg

logger=logging.getLogger(__name__)

#Now we are going to Set the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

#GPG encryption
gpg = gnupg.GPG(gpgbinary='C:\\Program Files (x86)\\gnupg\\bin\\gpg.exe')

def generateKey():
    """
        This function will generate public gpg key    
    """

    os.system('rm -rf /home/testgpguser/gpghome')
    input_data = gpg.gen_key_input(
        name_email='testgpguser@mydomain.com',
        passphrase='my passphrase')
    key = gpg.gen_key(input_data)

    return key

def exportKey():
    """
        This function will give public and private key    
    """
    key = generateKey()
    ascii_armored_public_keys = gpg.export_keys(key)
    ascii_armored_private_keys = gpg.export_keys(key, True)
    with open('mykeyfile.gpg', 'w') as f:
        f.write(ascii_armored_public_keys)
        f.write(ascii_armored_private_keys)

def importKey():
    """
        This function will use for importing keys file   
    """
    with open('mykeyfile.gpg','rb') as file:
        key_data = file.read()
    import_result = gpg.import_keys(key_data)
    gpg.trust_keys(import_result.fingerprints, 'TRUST_ULTIMATE')
    public_keys = gpg.list_keys()
    private_keys = gpg.list_keys(True)

    logger.debug('public keys:')
    logger.debug(public_keys)
    logger.debug('private keys:')
    logger.debug(private_keys)

    return import_result

def encryptString():
    """
        This function will use for encrypting strings   
    """
    import_result = importKey()
    unencrypted_string = 'Who are you? How did you get in my house?'
    encrypted_data = gpg.encrypt_file(
            string = unencrypted_string, recipients= import_result.fingerprints)
    encrypted_string = str(encrypted_data)

    logger.debug('ok: ', encrypted_data.ok)
    logger.debug('status: ', encrypted_data.status)
    logger.debug('stderr: ', encrypted_data.stderr)
    logger.debug('unencrypted_string: ', unencrypted_string)
    logger.debug('encrypted_string: ', encrypted_string)

def encryptFile():
    """
        This function will use for encrypting files   
    """
    import_result = importKey()
    open('my-unencrypted.txt', 'w').write('You need to Google Venn diagram.')
    with open('my-unencrypted.txt', 'rb') as file_loc:
        encrypted_data = gpg.encrypt_file(
            file= file_loc, recipients= import_result.fingerprints,
            output="encrypted-payload.pgp")

    logger.debug('ok: ', encrypted_data.ok)
    logger.debug('status: ', encrypted_data.status)
    logger.debug('stderr: ', encrypted_data.stderr)

def decryptString():
    """
        This function will use for decrypting strings   
    """
    import_result = importKey()
    unencrypted_string = 'Who are you? How did you get in my house?'
    encrypted_data = gpg.encrypt_file(
            string = unencrypted_string, recipients= import_result.fingerprints)
    encrypted_string = str(encrypted_data)
    decrypted_data = gpg.decrypt(encrypted_string, recipients= import_result.fingerprints)

    logger.debug('ok: ', decrypted_data.ok)
    logger.debug('status: ', decrypted_data.status)
    logger.debug('stderr: ', decrypted_data.stderr)
    logger.debug('decrypted string: ', decrypted_data.data)

def decryptFile():
    """
        This function will use for decrypting files   
    """
    import_result = importKey()
    open('my-unencrypted.txt', 'w').write('You need to Google Venn diagram.')
    with open('my-unencrypted.txt', 'rb') as f:
        decrypted_data = gpg.encrypt_file(
            f, recipients= import_result.fingerprints,
            output='my-encrypted.txt.gpg')

    logger.debug('ok: ', decrypted_data.ok)
    logger.debug('status: ', decrypted_data.status)
    logger.debug('stderr: ', decrypted_data.stderr)






