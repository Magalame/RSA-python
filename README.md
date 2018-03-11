# RSA-python
Basic implementation of RSA in python3

The main functions are 'encrypt(message, nlen, e, m)', which takes a message of arbitrary length, the size of the key, then e and m corresponding to the key.
And it outputs a list of binary strings, which corresponds to the message encrypted and split in order to suit the size of the key.

Then 'decrypt(message_encrypted_parts, nlen, d, m)' takes the output list of binazy string, then outputs the message decoded as a string. 
