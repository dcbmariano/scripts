#! /usr/bin/python26
#     Program: select.py
#    Function: escolhe um numero de seq
# Description: 
#      Author: Diego Mariano
#     Version: 1

from Bio import SeqIO
import sys
import os
import random


if(sys.argv[1] == '--help' or sys.argv[1] == '-h'):
	print "Syntax 'python select.py [file1] [file2] [num_seqs] [num_lines]'"
	sys.exit()

f1 = sys.argv[1]
f2 = sys.argv[2]
nseqs = int(sys.argv[3])
nlines = int(sys.argv[4])

print "Construindo matrix randomica de %d elementos." %(nseqs)

try:
	matrix = random.sample(xrange(nlines/4), nseqs)
except:
	print "FALHA: numero de sequencias deve ser menor"

print "Reduzindo %d sequencias para %d sequencias escolhidas aleatoriamente." %(nlines/4,nseqs)
matrix.sort()
#print matrix

# Abrindo sequencia f1
seqf1 = open(f1,'r')
seqf2 = open(f2,'r')

out1 = open("out1.fastq","w")
out2 = open("out2.fastq","w")

#Contador j: posicao atual na matrix; k permite uma contagem de linhas de 0 a 4
j = 0
k = 0

for i in range(0,nlines):
	# Laco percorre arquivos fastq pareados
	linef1 = seqf1.readline()
	linef2 = seqf2.readline()
	
	#condicoes para gravacao
	cod1 = int(i/4) 

	try:
		if(matrix[j] == cod1 or k > 0):
			# Grava as sequencias nos arquivos out
			out1.write(linef1)
			out2.write(linef2)

			# Contador de sequencias
			# Esse codigo foi ajustado para rodar da maneira mais rapida possivel... 
			# possivelmente nao me lembrarei como funciona, mas "Diego do futuro" pode confiar nele! :)
			
			k = k + 1
			if(k == 4):
				k = 0
				j = j + 1
	except:
		break

print "end"

out1.close()
out1.closed
out2.close()
out2.closed
