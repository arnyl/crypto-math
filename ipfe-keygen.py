"""ipfe-keygen.py"""
from Params import inn_product, list_gen
from time import time

def main_Keygen():
    print("\n===== IPFE KEYGEN =====")
    p = int(input('p: '))
    l = int(input('l: '))

    # pembangkitan y secara acak
    y = list_gen(p, l)
    print('y:', y)

    print('\nEnter the master secret key separated by comma')
    msk = list(map(int,input("msk: ").split(', ')))[:l]
    print('msk:', msk)
    
    print('\ngenerating private functional key...')
    start = time()
    sky = inn_product(y, msk)
    end = time()
    print('sky:', sky)
    print(f'time: {end-start}')

main_Keygen()



