#! /usr/bin/python26
#     Program: blastExtremidades.py
#    Function: Faz blast de dois arquivos contra a referencia
# Description: 
#      Author: Diego Mariano
#     Version: 1

from Bio import SeqIO
import sys
import os

if(sys.argv[1] == '--help' or sys.argv[1] == '-h'):
	print "Syntax 'python blastExtremidades.py [reference_file_name] [OPTIONAL name_file_left] [OPTIONAL name_file_right]'"
	sys.exit()

# Recebe as variaveis da chamada
file_name = sys.argv[1]

try:
	left = sys.argv[2]
except:
	left = 'end_seq_left.fasta'
try:
	right = sys.argv[3]
except:
	right = 'begin_seq_right.fasta'


# Extrai as sequencias, caso mude o arquivo de entrada
for i in SeqIO.parse(left,"fasta"):
	seq_left = str(i.seq)
for i in SeqIO.parse(right,"fasta"):
	seq_right = str(i.seq)

# Blast
query_left = "blastn -subject %s -query %s -outfmt '6 sstart' > tmp_left.txt" %(file_name,left)
query_right = "blastn -subject %s -query %s -outfmt '6 send' > tmp_right.txt" %(file_name,right)
cut_left = os.system(query_left)
cut_right = os.system(query_right)

print "Executado com sucesso."
