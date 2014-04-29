#! /usr/bin/python
#     Program: contigINFO.py
#    Function: Analisa funcoes de contigs - Le um arquivo multifasta e retorna informacoes sobre ele
# Description: le funcoes basicas do biopython, como ler sequencias
#      Author: Diego Mariano
#     Version: 2

from Bio import SeqIO
import sys

arquivo = sys.argv[1]
quant = 0
sumcontig = 0
maxcontig = 0
mincontig = None
nome_organismo = None

for i in SeqIO.parse(arquivo,"fasta"):

	# Tamanho do contig atual
	tam_contig = len(i.seq)

	# Pegando o menor contig na primeira rodada
	if mincontig is None:
		mincontig = len(i.seq)

	# Descobrindo o maior contig
	if tam_contig > maxcontig:
		maxcontig = tam_contig

	# Descobrindo o menor contig
	if tam_contig < mincontig:
		mincontig = tam_contig

	# Somando todos os elementos
	sumcontig = sumcontig + tam_contig

	# Descobrindo o total de contigs
	quant = quant + 1

	# Nome do organismo
	if nome_organismo is None:
		nome_organismo = i.name

# Agora vamos exibir os resultados
print "   File: ",arquivo
print "    Min: ",mincontig
print "    Max: ",maxcontig
print "  Bases: ",sumcontig
print "Contigs: ",quant