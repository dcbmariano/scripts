#! /usr/bin/python26
#     Program: multifile_scaf.py
#    Function: Recebe um arquivo multifasta e salva cada sequencia em um arquivo separado
# Description: 
#      Author: Diego Mariano
#     Version: 1
from Bio import SeqIO
import sys
import os
if(sys.argv[1] == '--help' or sys.argv[1] == '-h'):
	print "Syntax 'python multifile_scaf.py [seq]'"
	sys.exit()
sequence = sys.argv[1]
j = 0
print "Creating scaffolds files"
for i in SeqIO.parse(sequence,"fasta"):
	name = "scaf_%d" %j
	seq_ref = str(i.seq)
	q = open(name,'w')
	q.write(name)
	q.write("\n")
	q.write(seq_ref)
	q.close()
	q.closed
	j = j+1
print "end"
