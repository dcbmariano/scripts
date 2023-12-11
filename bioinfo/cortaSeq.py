#! /usr/bin/python26
#     Program: cortaSeq.py
#    Function: Corta uma string, retorna um arquivo com a nova sequencia, alem de um arquivo .qual 
# Description: 
#      Author: Diego Mariano
#     Version: 2

from Bio import SeqIO
import sys

if(sys.argv[1] == '--help' or sys.argv[1] == '-h'):
	print "Syntax 'python cortaSeq.py reference.fasta [OPTIONAL int begin] [OPTIONAL int end]'"
	sys.exit()

reference = sys.argv[1]

# Permite receber posicoes de corte ou buscar no output do script blastExtremidades.py
try:
	start = int(sys.argv[2])
	end = int(sys.argv[3])
except:
	s = open('tmp_left.txt','r')
	e = open('tmp_right.txt','r')
	start = int(s.readline())
	end = int(e.readline())
	s.closed
	e.closed	

# Pequena correcao na posicao de inicio
start = start-1

# Le genoma refecencia usando biopython
for i in SeqIO.parse(reference,"fasta"):
	ref = str(i.seq)

# Grava a sequencia extraida num arquivo fasta
saida = "out_cut_sequence.fasta"
w = open (saida,'w')
new_seq = ref.rstrip()[start:end]
len_ref = len(new_seq)
w.write(">seq\n")
w.write(new_seq)
w.close()
w.closed

# Grava um arquivo .qual (exigencia do mira)
saida_qual = "out_cut_sequence.fasta.qual"
q = open (saida_qual,'w')
q.write(">qual\n")
qual = ""
for i in range(0,len_ref):
	qual = "%s50 " %qual
q.write(qual)
q.close()
q.closed

print "Executado com sucesso."
