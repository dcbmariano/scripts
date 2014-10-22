#!/usr/bin/python
#     Program: hello world
#    Function: My first program 
# Description: lê funções básicas do biopython, como ler sequencias
#      Author: Diego Mariano
#     Version: 2

#import Bio
from Bio.Seq import Seq

seq = Seq("CATAATATA")
print(seq)
print(seq.translate())

# Minha primeira gambiarra em Python = invertendo uma sequencia
complement_reverse = seq.reverse_complement()
complement = complement_reverse.complement()
print complement

# Lendo um arquivo fasta
'''
from Bio import SeqIO
for seq_record in SeqIO.parse("o.fa","fasta"):
	print(seq_record.id)
	print(seq_record.seq)
	print(len(seq_record))
	print("\n")
print("\n\nFIM")
'''

# Agora a giripoca vai piar: vamos ler o GBK
from Bio import SeqIO
for seq_record in SeqIO.parse("o.gbk","genbank"):
	print(seq_record.id)
	print(repr(seq_record.seq))
	print(len(seq_record))
print "\n\nEND"