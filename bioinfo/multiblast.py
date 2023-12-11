#! /usr/bin/python
#     Program: multiblast.py
#    Function: 
# Description:
#      Author: Diego Mariano
#     Version: 1

from Bio import SeqIO
import sys
import os

try:
	arquivo1 = sys.argv[1]
	arquivo2 = sys.argv[2]
	fail = False
except:
	print "Syntax: 'python multiblast.py [query].fasta' [subject].fasta"
	fail = True

if fail == True:
	sys.exit()

if arquivo1 == "-h":
	print "Syntax: 'python multiblast.py [query].fasta' [subject].fasta"
	sys.exit()

cont = 0

for i in SeqIO.parse(arquivo1,"fasta"):
	cont = cont + 1
	tmp1 = open('tmp1',"w")
	query = str(i.seq)
	tmp1.write(query)
	tmp1.close()
	tmp1.closed
	cont2 = 0

	for k in SeqIO.parse(arquivo2,"fasta"):
		cont2 = cont2 + 1
		tmp2 = open('tmp2','w')
		subject = str(k.seq)
		tmp2.write(subject)
		tmp2.close()
		tmp2.closed

		#Blastn query
		print "\nExecutando BLAST query %d x contig %d" %(cont,cont2)
		comando = "blastn -subject tmp2 -query tmp1 -outfmt \"6 qseqid qlen qstart qend sseqid sstart send slen\" >> resultado.txt"
		os.system(comando)




