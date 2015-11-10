# dpair - Dictionary Password Attack in esreveR
A simple utility to create long and secure passphrases, based on
the methodology of dictionary attacks.

###Usage:

    >>> import dpair
    >>> dpair.gen()
    'RefreshTitledMariaHormoneCredit'
    >>> passphrase = dpair.gen(words=4, lower=True)
    >>> print passphrase
    queenboardsethernetgordon

https://xkcd.com/936/ - inspiration and giggles.

Special thanks to first20hours on Github for providing the wordlist used
in this module. (https://github.com/first20hours/google-10000-english)
