#!/bin/python

sequences = "tatgctttcc#tataggtctg#ctattcatt"
dna_list = sequences.split("#")
print (dna_list)

for dna in dna_list:
  rna = dna.replace("t", "u")
  print (f"DNA: {dna} -> RNA: {rna}")
