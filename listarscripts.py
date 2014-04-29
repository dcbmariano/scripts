#! /usr/bin/python
#     Program: listarScripts.py
#    Function: Lista todos os scripts contidos neste diretorio
# Description: Funciona apenas em sistemas UNIX
#      Author: Diego Mariano
#     Version: 4

import os
import sys

os.system("ls *.py > list_file_py.txt")
arquivo = open("list_file_py.txt","r")
line = 0
parametro = 0
try:
        parametro = sys.argv[1]
        print "\n######################## File | Function | Description ########################\n"
except:
        print "\n############################# File | Function #############################\n"

if parametro == "-h":
        print "HELP ||||||||||||||||||||||||||||||||\nlistarScripts | Sintaxe: python listarscripts.py | Use [-d] to list description\n"
        sys.exit()

while line != "":
        line = arquivo.readline()
        line = line.rstrip("\n\r")
        if line != "listarscripts.py" and line != "":
                arq_ind = open(line,"r")
                info = arq_ind.readlines()
                program = line
                function = info[2].rstrip("\n\t")
                function = function[15:]
                if parametro == "-d":
                        desc = info[3].rstrip("\n\t")
                        desc = desc[2:]
                        print program," | ",function,"\n",desc,"\n"
                else:
                        print program," | ",function
print ""

