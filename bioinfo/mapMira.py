#! /usr/bin/python26
#     Program: mapMira.py
#    Function: Recebe a sequencia e faz um novo mapeamento do mira
# Description: 
#      Author: Diego Mariano
#     Version: 1

from Bio import SeqIO
import sys
import os

if(sys.argv[1] == '--help' or sys.argv[1] == '-h'):
	print "Syntax 'python mapMira.py [seq] [OPTIONAL name] [OPTIONAL raw_fastq] [OPTIONAL seq_qual] [OPTIONAL raw_xml]'"
	sys.exit()

# Recebe sequencia referencia
try:
	sequence = sys.argv[1]
except:
	sequence = 'out_cut_sequence.fasta'

# Recebe NOME PROJETO
try:
	name_project = sys.argv[2]
except:
	name_project = 'map'

# Recebe dados brutos FASTQ
try:
	raw_data_fastq = sys.argv[3]
except:
	raw_data_fastq = "../../*.fastq"

# Recebe XML
try:
	raw_data_xml = sys.argv[4]
except:
	raw_data_xml = "../../*.xml"
	
# Modelo manifest OPTIONAL \nparameters = -AS:urd=yes
manifest = "project = %s \njob = genome,mapping,accurate \n\nreadgroup \nis_reference \ndata = %s\n\nreadgroup = fragment \ntechnology = iontor \ndata = %s %s" %(name_project,sequence,raw_data_fastq,raw_data_xml)

print manifest

m = open('map.manifest','w')
m.write(manifest)
m.close()
m.closed

command = "mira4.0 map.manifest"

os.system(command)

print "Executado com sucesso."
