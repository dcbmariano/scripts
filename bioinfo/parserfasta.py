#!/usr/bin/python
#     Program: parserFasta.py
#    Function: Ler um arquivo fasta e retirar apenas o genero necessario
# Description:
#      Author: Diego Mariano
#     Version: 1

from Bio import SeqIO
import sys

cont = 0

try:
	arquivo = sys.argv[1]
	genero = sys.argv[2]
	fail = False
except:
	print "Sintaxe: 'python parserfasta.py [file_name].fasta'"
	fail = True

name_out = "%s_out.fasta" %genero
out = open(name_out,"w")
out.close()

if fail == True:
	sys.exit()

for i in SeqIO.parse(arquivo,"fasta"):
	valores = i.description.rsplit("=")
	valor_genero = valores[1].rsplit(" ")
	if valor_genero[0] == genero:
		out = open(name_out,"a")
		descricao = ">%s \n" %i.description
		out.write(descricao)
		out.close()
		out = open(name_out,"a")
		sequency = str(i.seq)
		sequency += "\n"
		out.write(sequency)
		out.close()
		cont += 1
out.closed

print "%d sequencias lidas." %cont
print "Executado com sucesso :)"