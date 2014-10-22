from Bio import SeqIO
import sys

w = open('result.fasta','w')
p = sys.argv[1]

for i in SeqIO.parse(p,"fasta"):
	seq = str(i.seq)
	w.write(seq)
	w.write('N')
w.close()
w.closed
	

