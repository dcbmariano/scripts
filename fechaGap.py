#! /usr/bin/python26
#     Program: fechaGap.py
#    Function: Recebe um arquivo multifasta, 2 contigs sequenciais e dado extraido
# Description: 
#      Author: Diego Mariano
#     Version: 1

from Bio import SeqIO
import sys
import os

if(sys.argv[1] == '--help' or sys.argv[1] == '-h'):
	print "Syntax 'python fechaGap.py [seq] [contig left name] [contig right name] [OPTIONAL result mira]'"
	sys.exit()

# Recebe sequencia referencia
sequence = sys.argv[1]
left = sys.argv[2]
right = sys.argv[3]
left_file = "end_seq_left.fasta"
right_file = "begin_seq_right.fasta"

l = open(left_file,'r')
left_seq = l.readline()

r = open(right_file,'r')
right_seq = r.readline()

# Recebe resultado mira
try:
	result_mira = sys.argv[4]
except:
	result_mira = "map_assembly/map_d_results/map_out_ReferenceStrain.unpadded.fasta"

# remove as sequencias repetidas do resultado do mira
for i in SeqIO.parse(result_mira,"fasta"):
	seq_mira = str(i.seq)

# Sera necessario refazer o BLAST
query_left = "blastn -subject %s -query %s -outfmt '6 send' > tmp_A.txt" %(result_mira,left_file)
query_right = "blastn -subject %s -query %s -outfmt '6 sstart' > tmp_B.txt" %(result_mira,right_file)
os.system(query_left)
os.system(query_right)
tmpA = open('tmp_A.txt','r')
tmpB = open('tmp_B.txt','r')
cut_left = int(tmpA.readline())
cut_left = cut_left+1
cut_right = int(tmpB.readline())
tmpA.close()
tmpA.closed
tmpB.close()
tmpB.closed

seq_mira = seq_mira[cut_left:cut_right]

# REMOVE O GAP
sf = open(sequence,'r')
genome = sf.read()
remove_contig_id = ">%s" %(right)
gap_closed = genome.replace(remove_contig_id,seq_mira)

sf.close()
sf.closed

g = open('out_genome_gap_closed.fasta','w')
g.write(gap_closed)
g.close()
g.closed

print "Executado com sucesso."
