#/usr/bin/env python

"""
dpair - Dictionary Password Attack in esreveR
----------------------------------------------

A simple utility to create long and secure passphrases, based on
the methodology of dictionary attacks.

Usage:

    >>> import dpair
    >>> dpair.gen()
    'RefreshTitledMariaHormoneCredit'
    >>> passphrase = dpair.gen(words=4, lower=True)
    >>> print passphrase
    queenboardsethernetgordon

https://xkcd.com/936/ - inspiration and giggles.

Special thanks to first20hours on Github for providing the wordlist used
in this module. (https://github.com/first20hours/google-10000-english)

"""

import os
import random

def get_word_list(custom_wordlist=None):
    "Finds path of wordlist to be used; confirms it is a valid file."
    if custom_wordlist and os.path.isfile(custom_wordlist):
        wordlist = custom_wordlist
    else:
        wordlist = os.path.join(os.path.dirname(__file__), 'assets', 'google-10000-english.txt')

    try:
        if not os.path.isfile(wordlist):
            raise IOError
        else:
            return wordlist
    except IOError:
        print("[!] Cannot find usable wordlist!\n")


def word_generator(wordlist, words=5):
    "Returns generator of entire wordlist for efficient word selection."
    with open(wordlist) as w:
        choices = list(w)

        for n in range(words):
            rand_word = random.randint(0, len(choices))
            yield choices[rand_word].strip('\n')
            # One-liner for above 2 lines, but less pretty and readable:
            # yield choices[random.randint(0, len(choices))].strip('\n')


def gen(words=5, min_length=20, lower=False, custom_wordlist=None):
    "Generates passphrase using randomly selected words."
    # Like a dictionary password attack in reverse!!!
    wordlist = get_word_list(custom_wordlist)
    passphrase = ''

    while len(passphrase) < min_length:
        passphrase = ''
        dictionary_choices = word_generator(wordlist, words)

        phrase_list = []

        for w in dictionary_choices:
                current = w[0].upper() + w[1:]
                phrase_list.append(current)

        passphrase = ''.join(phrase_list)

    # Make entire passphrase lowercase. Not recommended for obvious reasons
    if lower:
        passphrase = passphrase.lower()

    return passphrase
