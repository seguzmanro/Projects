'''
This little program helps in generating random nucleotide sequences of arbitrary lenght.
These sequences may be used to test other programs/pipelines.
'''
import random


def simul_seq(lenght_of_the_sequence):
    brute_res = []
    for i in range(lenght_of_the_sequence):
        brute_res.append(random.choice(['a','g','c','t']))
    seq = ''.join(brute_res)
    return seq


if __name__ == '__main__':
    lenght_of_the_sequence = int(input('Longitud de la sencuencia: '))

    print(simul_seq(lenght_of_the_sequence))
