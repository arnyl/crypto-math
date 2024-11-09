"""ipfe-decrypt.py"""
from Params import get_data
from time import time
import math

def main_Decrypt():
    print("\n===== IPFE DECRYPTION =====")
    p = int(input('p: '))
    g = int(input('g: '))
    l = int(input('l: '))

    print('\nEnter the vector key (y) separated by comma')
    y = list(map(int,input("y: ").split(', ')))[:l]
    print('y:', y)

    print('\nEnter the private functional key separated by comma')
    sky = int(input('sky: '))
  
  
    print('\nEnter the ciphertext separated by comma')
    ct0 = int(input('ct0: '))
    cti = list(map(int,input("cti: ").split(', ')))[:l]
    
    start = time()
    m = get_data(g, y, sky, ct0, cti)
    end = time()

    print('m:', m)
    print(f'time: {end-start}')

main_Decrypt()
