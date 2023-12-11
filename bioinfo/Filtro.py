#!/usr/bin/python

from datetime import datetime

arquivo1 = open("/data/lpdna/cp31/5500/dados_brutos/F3.csfasta")
arquivo2 = open("/data/lpdna/cp31/5500/dados_brutos/F3.QV.qual")
saida = open("/data/lpdna/cp31/5500/filtrados/F3_QV30_PY.csfasta.", "w")
contador = 0

cabecalho = "1"

print datetime.now()

while cabecalho != "":
	cabecalho = arquivo1.readline()
	qualidade = arquivo2.readline()
	if cabecalho != "":
		if cabecalho[0] == '>':
			qualidade = arquivo2.readline()
			soma = 0
			numero = ""
			for char in qualidade:
				if char == ' ':
					soma = soma + int(numero)
					numero = ""
				numero = numero + char
			media = soma / 35.
			sequencia = arquivo1.readline()
			if media >= 30:
				contador = contador + 1
				saida.write(cabecalho)
				saida.write(sequencia)
print datetime.now()
