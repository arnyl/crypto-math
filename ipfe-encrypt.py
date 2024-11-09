"""Encrypt.py"""
from random import randint
from Params import get_ctx
import time

def main_Encrypt():
    print("\n===== IPFE ENCRYPTION =====")
    p = int(input('p: '))
    g = int(input('g: '))
    l = int(input('l: '))
    
    r = randint(2, p)
    print(f'r: {r}')
    print('\nEnter the public key separated by comma')
    mpk = list(map(int,input("mpk: ").split(', ')))[:l]
    print('mpk: ', mpk)
   
    print('\nEnter the plaintext separated by comma')
    ptx = list(map(int,input("ptx: ").split(', ')))[:l]
    print('ptx: ', ptx)
    print('\nencrypting ...')
    
    start = time.time()
    ctx = get_ctx(g, r, mpk, ptx)
    end = time.time()
    print(f'ctx = (c0, cti) = {ctx}')
    print(f'time: {end-start}')

main_Encrypt()
