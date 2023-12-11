#! /usr/bin/python
#     Program: gapINFO.py
#    Function: Analisa arquivos de scaffolds
# Description: Contem informacoes de como usar parametros de chamada [melhoria no controle de parada], biopython e controle de excessoes
#      Author: Diego Mariano
#     Version: 1

from Bio import SeqIO
import sys

p1 = 0
line = 0
lines = ""
line = 0
contigs = 0
gaps = 0

try:
	p1 = sys.argv[1]
except:
	print "HELP: Use 'python gapINFO [name_file].fasta'"

if p1 == "-h":
	print "HELP: Use 'python gapINFO [name_file].fasta'"
	sys.exit()

if p1 == 0:
	sys.exit()

for i in SeqIO.parse(p1,"fasta"):
	seq_final = i.seq

seq_f_s = seq_final.split("N")

out = "%s_out.fasta" %p1

w = open(out,"w")
w.close()
for item in seq_f_s:
	a = str(item)
	print a
	if a != "N":
		print contigs
		contig = ">contig_%d" %contigs
		w = open(out,"a")
		w.write(contig)
		w.close()
		w = open(out,"a")
		w.write(a)
		w.close()
		contigs = contigs + 1
w.closed
