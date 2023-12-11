#! /usr/bin/python26
#     Program: convertemultifasta.py
#    Function: Converter arquivos multifasta em arquivo com uma unica sequencia
# Description: Recebe um arquivo multifasta, elimina os cabecalhos e os substitui por 100 Ns
#      Author: Diego Mariano
#     Version: 1

from Bio import SeqIO
import sys

w = open('scaffold.fasta','w')
p = sys.argv[1]
w.write('>scaffold')

for i in SeqIO.parse(p,"fasta"):
	seq = str(i.seq)
	w.write(seq)
	w.write('NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN')
	
w.close()
w.closed
	

