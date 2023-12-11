#!/usr/bin/python
#     Program: construirDBsBlast.py
#    Function: Constroi os bancos de dados usados pelo Blast atraves de um arquivo fasta
# Description:
#      Author: Diego Mariano
#     Version: 1

import sys
import os

try:
	arg1 = sys.argv[1]
except:
	arg1 = None

if arg1 is None or arg1 is "-h":
	print "Sintaxe: 'python construirdbblast.py [file_name].fasta'"
	sys.exit()	

try:
	open(arg1,'r')
except:
	print "File not found."
	sys.exit()

name = arg1.rsplit(".")

print "Construindo a database %s" %name[0]

query = "makeblastdb -in %s -input_type fasta -dbtype prot -out %s_db -max_file_sz 1000MB -parse_seqids" %(arg1,name[0])

os.system(query)
os.system("pwd")
print "Concluido com sucesso."
