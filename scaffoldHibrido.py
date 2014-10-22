#! /usr/bin/python26
#     Program: scaffoldHibrido.py
#    Function: Fecha um gap com base em uma outra tentativa de montagem
# Description: 
#      Author: Diego Mariano
#     Version: 1

from Bio import SeqIO
import sys
import os
 
# Helper
try:
	if(sys.argv[1] == '--help' or sys.argv[1] == '-h'):
		print "Syntax 'python scaffoldHibrido.py [contigs_file_1] [contig_gap_left] [contig_gap_right] [contigs_file_2] [contig_reference]'"
		sys.exit()
except:
	print "Syntax error. \nSyntax 'python scaffoldHibrido.py [contigs_file_1] [contig_gap_left] [contig_gap_right] [contigs_file_2] [contig_reference]'"
	sys.exit()

# Recebe as variaveis da chamada
contigs_file_1 = sys.argv[1]
contig_gap_left = sys.argv[2]
contig_gap_right = sys.argv[3]
contigs_file_2 = sys.argv[4]
contig_reference = sys.argv[5]

print "\n------------------------- Running scaffoldHibrido -------------------------"

# -------------------------------------------------------------------------------------------------------------------------------
# 
# Separa contigs
#
# -------------------------------------------------------------------------------------------------------------------------------

# Extrai os contigs proximos ao gap - CONTIGS FILE 1
for i in SeqIO.parse(contigs_file_1,"fasta"):
	if(i.id == contig_gap_left):
		seq_left = str(i.seq)
	if(i.id == contig_gap_right):
		seq_right = str(i.seq)

# Reduz tamanho da sequencia - max. 5000
tam_seq_left = len(seq_left)
tam_seq_right = len(seq_right)

if(tam_seq_left > 5000):
	seq_left = seq_left[-5000:]

if(tam_seq_right > 5000):
	seq_right = seq_right[:5000]

# Grava sequencia esquerda
l = open('tmp_seq_left.txt','w')
l.write(seq_left)
l.close()
l.closed

# Grava sequencia direita
r = open('tmp_seq_right.txt','w')
r.write(seq_right)
r.close()
r.closed

# Extrai contig referencia - CONTIGS FILE 2
for i in SeqIO.parse(contigs_file_2,"fasta"):
	if(i.id == contig_reference):
		seq_ref = str(i.seq)

# Grava sequencia referencia
r = open('tmp_seq_ref.txt','w')
r.write(seq_ref)
r.close()
r.closed

# IMPORTANTE: as sequencias a ser analisadas estao em arquivos 
print "\nStep 1/5 \nSuccess."


# -------------------------------------------------------------------------------------------------------------------------------
# 
# BLAST para verificacao se existe sobreposicao e definir pontos de corte
#
# -------------------------------------------------------------------------------------------------------------------------------

# Efetua consultas blast e retorna os as posicoes
query_left = "blastn -subject tmp_seq_ref.txt -query tmp_seq_left.txt -outfmt '6 send' > tmp_left_end.txt" 
query_right = "blastn -subject tmp_seq_ref.txt -query tmp_seq_right.txt -outfmt '6 sstart' > tmp_right_start.txt" 
cut_left = os.system(query_left)
cut_right = os.system(query_right)

# Le o arquivo e pega apenas o melhor resultado 
s = open('tmp_left_end.txt','r')
e = open('tmp_right_start.txt','r')
begin_cut_reference = int(s.readline())
end_cut_reference = int(e.readline())
s.closed
e.closed

# Pequena correcao na posicao de inicio
begin_cut_reference = begin_cut_reference+1

# IMPORTANTE: pontos de corte armazenados em begin_cut_reference e end_cut_reference
print "\nStep 2/5 \nSuccess."


# -------------------------------------------------------------------------------------------------------------------------------
# 
# Corta regiao delimitada na referencia
#
# -------------------------------------------------------------------------------------------------------------------------------

# Faz os cortes no genoma e grava a sequencia extraida num arquivo fasta
new_seq = seq_ref.rstrip()[begin_cut_reference:end_cut_reference]

# IMPORTANTE: 
print "\nStep 3/5 \nSuccess."

# -------------------------------------------------------------------------------------------------------------------------------
# 
# Transfere a sequencia extraida para fechar o gap inicial
#
# -------------------------------------------------------------------------------------------------------------------------------

# REMOVE O GAP
sf = open(contigs_file_1,'r')
genome = sf.read()
remove_contig_id = ">%s" %(contig_gap_right)
gap_closed = genome.replace(remove_contig_id,new_seq)

sf.close()
sf.closed

name_final = "final_seq_gap_closed_%s_%s.fasta" %(contig_gap_left,contig_gap_right)
g = open(name_final,'w')
g.write(gap_closed)
g.close()
g.closed

# IMPORTANTE: 
print "\nStep 4/5 \nSuccess."

# -------------------------------------------------------------------------------------------------------------------------------
# 
# Remove TMP files
#
# -------------------------------------------------------------------------------------------------------------------------------

command = "rm -rf tmp_*"
os.system(command)
print "\nStep 5/5 \nSuccess"

print "\nResult: final_seq_contigs.fasta\n"
print "Success"
