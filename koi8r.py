#!/usr/bin/env python3
def koi8r(text):
    idx = 7
    bit = 0
    msk = ~(1 << idx)
    return [
        chr((num & msk) | (bit << idx)) for num in text.encode("koi8-r")
    ]

print(koi8r("Привет, Мир!"))
print(koi8r("Кодировки это весело! Ведь да?"))
