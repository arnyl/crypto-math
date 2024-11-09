"""ipfe-setup.py"""
from Params import gen_prime, generators, list_gen, setup
import random
from time import time
from random import choice


def main_Setup():
    print("\n===== IPFE SETUP =====")
  

    p = gen_prime() #size 2^8 dapat diubah pada Params
    print(f'p: {p}')
    gens = generators(p)
    g = choice(gens)
    print('g:', g)
    l = int(input('l: ' ))

    #membangkitkan kunci secara acak 
    msk = list_gen(p, l) 
    
    start = time()
    mpk = setup(msk, g)
    end = time()

    print('generating .... ')
    print(f'(msk, mpk) = ({msk}, {mpk})')
    print(f'time: {end-start}')

main_Setup()
