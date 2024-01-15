#!/usr/bin/env python

from string import *
from itertools import product

value = digits # ascii_letters + digits + punctuation

for i in range(1, 5):

  for j in product(value, repeat = i):
    word = "".join(j)

    if len(word) == 4 : # 4 digits number are stored in wordlists
      p = open("wordlists.txt", "a")
      p.write(word)
      p.write("\n")
