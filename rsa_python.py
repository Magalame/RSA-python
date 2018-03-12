import random
from timeit import timeit
import sys
from math import gcd
import string

def printf(text):
    sys.stdout.write(str(text)+"\n")
    sys.stdout.flush()

#returns the powers that rabbin mille
def puissances_miller(nb):
    puissances = []
    while nb%2 == 0:
        nb=nb//2
        #printf(nb)
        puissances.append(nb)
    if len(puissances) == 0:
        return [nb]
    else:
        return puissances

#implementation of miller rabbin
#we put the 'puissances' as argument so that we don't have to recompute it everytime
def mr_prime_test(n, puissances):
    
    a = random.randint(2,n-1)
    pow1 = pow(a,puissances[-1],n)
    
    if pow1 == 1:
        return True
    elif pow1 == n-1:
        return True
    
    for i in reversed(puissances[:-1]):
        
        result = pow(a,i,n)
        if result == n-1:
            return True      
   
    return False

def is_prime(n):

#------------------pre testing
   
    if not n & 1:
        return False
    
    if n<103:
        bound = n-3
    else:
        bound = 100
        
#------------------actual miller
    
    puissances = puissances_miller(n-1)
    for i in range(0,bound):
        if mr_prime_test(n, puissances):
            pass
        else:
            return False
    return True


#https://csrc.nist.gov/csrc/media/publications/fips/186/3/archive/2009-06-25/documents/fips_186-3.pdf  

def prime_gen(nlen):

    while True:
            n = random.randint(int((2**0.5)*(2**(nlen/2-1)))+1,int(2**(nlen/2))-1)
            if n & 1:
                break
            
    while not is_prime(n):
        n = n+2   
    return n

#https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python 
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
    
def random_string(length):
   return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

def create_rsa_keys(nlen):
    p,q = 0,0
    while abs(p-q) <= int(2**(nlen/2-100)):
        p = prime_gen(nlen)
        q = prime_gen(nlen)
    phi = (p-1)*(q-1)
    m=p*q
    while True:
        e = random.randint(2**16+1,2**256-1)
        if e & 1:
            if gcd(e,phi) == 1:
                break
    d = modinv(e, phi)
    return e,d,m

def encrypt(message, nlen, e, m):
    
    bound = nlen//8
    
    message_split = [message[i:i+bound] for i in range(0, len(message),bound)]
    
    message_encrypted_parts = []
    
    for i in range(0,len(message_split)):
        message_encrypted_parts.append(pow(int.from_bytes(message_split[i].encode("utf8"), byteorder='little'),e,m))
        
    return message_encrypted_parts

def decrypt(message_encrypted_parts, nlen, d, m):
    
    bound = nlen//8
    
    message_decrypted_parts = []
    
    for i in range(0,len(message_encrypted_parts)):
        message_decrypted_parts.append(pow(message_encrypted_parts[i],d,m).to_bytes(bound, byteorder='little').decode("utf8").rstrip('\0'))
        
    message = ''.join(message_decrypted_parts)
    
    return message


    
    


