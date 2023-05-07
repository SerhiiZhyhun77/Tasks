# -*- coding: utf-8 -*-

cipher = {
    'A': 'q',
    'B': 'w',
    'C': 'e',
    'D': 'r',
    'E': 't',
    'F': 'y',
    'G': 'u',
    'H': 'i',
    'I': 'o',
    'J': 'p',
    'K': 'l',
    'L': 'k',
    'M': 'j',
    'N': 'h',
    'O': 'g',
    'P': 'f',
    'Q': 'd',
    'R': 's',
    'S': 'a',
    'T': 'z',
    'U': 'x',
    'V': 'c',
    'W': 'v',
    'X': 'b',
    'Y': 'n',
    'Z': 'm',
    'a': 'Q',
    'b': 'W',
    'c': 'E',
    'd': 'R',
    'e': 'T',
    'f': 'Y',
    'g': 'U',
    'h': 'I',
    'i': 'O',
    'j': 'P',
    'k': 'L',
    'l': 'K',
    'm': 'J',
    'n': 'H',
    'o': 'G',
    'p': 'F',
    'q': 'D',
    'r': 'S',
    's': 'A',
    't': 'Z',
    'u': 'X',
    'v': 'C',
    'w': 'V',
    'x': 'B',
    'y': 'N',
    'z': 'M'
}


def code(text):
    ciphertext = ''
    for s in text:
        if s in cipher:
            ciphertext += cipher.get(s, '')
        else:
            ciphertext += s
    return ciphertext


def decode(ciphertext):
    deciphered_text = ''
    for s in ciphertext:
        letter = ''
        for key, val in cipher.items():
            if s == val:
                letter = key
        deciphered_text += letter if letter else s
    return deciphered_text
