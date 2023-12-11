#!/usr/bin/python
#     Program: rfi.py
#    Function: [REFERENCEinator2] Define a melhor referencia dado um arquivo multifasta 
# Description:
#      Author: Diego Mariano
#     Version: 2

from Bio import SeqIO
import sys
import os
import sqlite3

cont = 0

try:
	arquivo = sys.argv[1]
	fail = False
except:
	print "Syntax: 'python parserfasta.py [file_name].fasta'"
	fail = True

if fail == True:
	sys.exit()

if arquivo == "-h":
	print "Syntax: 'python parserfasta.py [file_name].fasta'"
	sys.exit()

cont = 0
cont2 = 0

for i in SeqIO.parse(arquivo,"fasta"):
	cont = cont + 1

for i in SeqIO.parse(arquivo,"fasta"):
	print "%s/%s" %(cont2,cont)
	cont2 = cont2 + 1
	out = open("tmp","w")
	seq = str(i.seq)
	out.write(seq)
	out.close()
	query = "blastn -remote -db nr -query \"tmp\" -outfmt \"6 sacc score\" >> results_blast.txt"
	os.system(query)