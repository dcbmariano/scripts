#! /usr/bin/python26
#     Program: reverteContig.py
#    Function: Recebe uma contig e inverte ela
# Description: 
#      Author: Diego Mariano
#     Version: 1

from Bio import SeqIO
import sys

arquivo = sys.argv[1]

# Invertendo o contig: 
for i in SeqIO.parse(arquivo,"fasta"):
	# Gerar complemento revertido
	reverse = i.reverse_complement()
	# Gerar complemento do complemento revertido
	#reverse = complement_reverse.seq.complement()

out_name = "%s_out.fasta" %arquivo

reverse = str(reverse.seq)

out = open(out_name,"w")
out.write(reverse)
out.close()
out.closed

print "Contig revertida com sucesso."
print "Arquivo disponivel em %s" %out_name
	
