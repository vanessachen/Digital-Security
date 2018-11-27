import multiprocessing
from hashlib import sha256
import time

char_length = 3

def HashFromSerial(serial):

    divisor = 26**(char_length-1)
    letters = []
    for i in range(char_length):
        letter, serial = divmod(serial, divisor)
        letters.append( 97 + int(letter) )
        divisor /= 26
    return (letters, sha256(bytes(letters)).digest())


def main():
    h1 = bytes().fromhex("40685fd53d8eb3b1e921f974d806fc800233fe75eda796aef4ed3964ba5b9238") #hi
    #h2 = bytes().fromhex("3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b")
    #h3 = bytes().fromhex("74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f")
    numpasswords = int(26 ** char_length)
    chunksize = int(numpasswords / multiprocessing.cpu_count())
    with multiprocessing.Pool() as p:
        for (letters, digest) in p.imap_unordered(HashFromSerial, range(numpasswords), chunksize):
            if digest == h1:
            #or digest == h2 or digest == h3:
                password = "".join(chr(x) for x in letters)
                print(password + " => " + digest.hex())


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print("Time Running: ", (end_time-start_time))
