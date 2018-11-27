#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, string, sys
import itertools, hashlib

def decrypter(hashed, chrs, min_length, max_length):
    if min_length > max_length:
        print ('\n Min-length must be longer than Max-length or as same as with Max-length.\n')
        sys.exit()

    end_result_chip = ''

    try:
        for n in range(min_length, max_length+1):
            for xs in itertools.product(chrs, repeat=n):
                result_chip = ''.join(xs)
                hash_chip = improt_module(result_chip).hexdigest()
                if hashed == hash_chip:
                    end_result_chip += result_chip
                    print ('Decrypt found : {}'.format(end_result_chip))
                    print ('End time      : {}\n'.format(time.strftime('%H:%M:%S')))
                    sys.exit()
                else:
                    print ('   *** Please drink your coffee first! ***')
                    print ('\t{} {}\n'.format(NAME, VERSION))
                    print ('CTRL+C to Exit!')
                    print ('Charachters to try : {}'.format(chrs))
                    print ('Min-length         : {}'.format(min_length))
                    print ('Max-length         : {}'.format(max_length))

                    print ('Trying with        : {} - {}'.format(result_chip, hash_chip))
                    time.sleep(0.01)
                    print("\033c")
    except KeyboardInterrupt:
        print ('Finished!\n')
        sys.exit()

    if end_result_chip == '':
        print ('Not Found!')
        print ('End time: {}\n'.format(time.strftime('%H:%M:%S')))
        sys.exit()
    else: pass

if __name__ == '__main__':
        try:
            len_hases = len(sys.argv[2])
            decrypter(sys.argv[1], CHRS, int(sys.argv[3]), int(sys.argv[4]))
