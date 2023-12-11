#! /usr/bin/python26
#     Program: selecionaExtremidades.py
#    Function: Recebe dois contigs, corta 5 mil pares de base de cada extremidade
# Description: 
#      Author: Diego Mariano
#     Version: 1

from Bio import SeqIO
import sys

if(sys.argv[1] == '--help' or sys.argv[1] == '-h'):
	print "Syntax 'python selecionaExtremidades.py [file_name] [name_contig_left] [name_contig_right]'"
	sys.exit()

# Recebe as variaveis da chamada
file_name = sys.argv[1]
left = sys.argv[2]
right = sys.argv[3]

# Extrai as sequencias
for i in SeqIO.parse(file_name,"fasta"):
	if(i.id == left):
		seq_left = str(i.seq)
	if(i.id == right):
		seq_right = str(i.seq)

# Reduz tamanho da sequencia - max. 5000
tam_seq_left = len(seq_left)
tam_seq_right = len(seq_right)

if(tam_seq_left > 5000):
	seq_left = seq_left[-5000:]

if(tam_seq_right > 5000):
	seq_right = seq_right[:5000]

# Grava sequencia esquerda
l = open('end_seq_left.fasta','w')
l.write(seq_left)
l.close()
l.closed

# Grava sequencia direita
r = open('begin_seq_right.fasta','w')
r.write(seq_right)
r.close()
r.closed

print "Executado com sucesso."
