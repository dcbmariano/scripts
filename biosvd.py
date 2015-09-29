#Autor: Thiago da Silva Correia

#!/usr/bin/python

from Bio import SeqIO
from Bio import Cluster
import numpy as np
import scipy.sparse
from numpy import array,vstack
import matplotlib.pyplot as plt
from numpy import linalg as LA
import subprocess
import random
import time
import os
import sys
from mpl_toolkits.mplot3d import Axes3D


#Controle do tempop de exucucao
ini = time.time()
TotalKMER = 8000;
FileNomeModelo = ''
FileNomeFamiliaModelo = ''
FileNomeQuery = ''
FileNomeFamiliaQuery = ''

i = 1
while i < (len( sys.argv)):
	if( sys.argv[i] == '-m1'):
		FileNomeModelo = sys.argv[i+1]
	if( sys.argv[i] == '-m2'):
		FileNomeFamiliaModelo = sys.argv[i+1]
	if( sys.argv[i] == '-q1'):
		FileNomeQuery = sys.argv[i+1]
	if( sys.argv[i] == '-q2'):
		FileNomeFamiliaQuery = sys.argv[i+1]
	i = i+2

print "Ordenando Seq"
command = "python OrdenarSeq.py"
os.system(command)

print "Iniciando Clustrizacao"

#Abrindo os arquivos necessario
FileModelo = open("SeqModeloAgrupadas.fasta", 'rU')	#Contem as sequencias do modelo
#FileModeloFamilia = open("yes.tab", 'rU') #Familias do modelo
FileQuery = open("SeqQueryAgrupadas.fasta", 'rU')	#Contem as sequencias das query
#FileQueryFamilia = open("no.tab", 'rU') #Familias do modelo

Filemat = open("Matriz.txt", 'w')#Matriz obtida do SVD. Matriz das posicoes do espaco 3D

FamiliasModelo = []
DistribuicaFamiliasModelo = []
NumFamiliasModelo = 0

FamiliasQuery = []
DistribuicaFamiliasQuery = []
NumFamiliasQuery = 0


#Lendo cabecalho os arquivos
NumFamiliasModelo = FileModelo.readline()
NumFamiliasQuery = FileQuery.readline()

print "Lendo cabecalho"
i =0
while( i< int(NumFamiliasModelo)):
	temp = FileModelo.readline();
	FamiliasModelo.append( temp.rstrip() )
	temp = FileModelo.readline();
	DistribuicaFamiliasModelo.append( temp )
	i = i+1
	
i =0
while( i< int(NumFamiliasQuery)):
	temp = FileQuery.readline();
	FamiliasQuery.append( temp.rstrip() )
	temp = FileQuery.readline();
	DistribuicaFamiliasQuery.append( temp )
	i = i+1

print "Fazendo o PARSE"
# Aqui faremos um PARSE dos arquivos .fasta para obter as sequencias a serem trabalhas
sequenciasModelo = list(SeqIO.parse(FileModelo, "fasta"))
sequenciasQuery = list(SeqIO.parse(FileQuery, "fasta"))

FileModelo.close()
FileQuery.close()
os.remove("SeqModeloAgrupadas.fasta")
os.remove("SeqQueryAgrupadas.fasta")


tamanhosequenciasModelo = len(sequenciasModelo)
NumroDeSequencias = tamanhosequenciasModelo + len(sequenciasQuery)
#print NumroDeSequencias

aminoacidos = [ 'A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I','L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V' ]
KMERPADRAO = []
HashKMer = {}

t=0
print "Gerando KMERS"
#Gerando todos os KMERS possiveis
for i in aminoacidos:
	for j in aminoacidos:
		for k in aminoacidos:
			KMERPADRAO.append( i+j+k )
			HashKMer[i+j+k] = t
			t = t+1
#print "Tamanho do hash"	
#print len(HashKMer)

print 'Juntando as listas'
#Matriz com 8000 linhas(Kmers de tamanha 3))
mat8000x200 = np.zeros(shape=(TotalKMER, NumroDeSequencias))
print mat8000x200.shape

allSequences = []

#Jutando todas as sequencias numa so lista
for i in sequenciasModelo:
	allSequences.append(i)
for i in sequenciasQuery:
	allSequences.append(i)
	
#Apagando as lista que nao serao mais usadas
del sequenciasModelo[:]
del sequenciasQuery[:]

print 'Preenchendo a Matriz Kmers'
for j in range(NumroDeSequencias):
		for k in range( len(allSequences[j]) -2):
			#Kmer contem algum aminoacidos fora dos 20 que estamos usando. Vamos ignorar tal kmer
			if str(allSequences[j].seq[k:k+3]) in HashKMer: # O preenchimento e por coluna
				i = HashKMer.get(str(allSequences[j].seq[k:k+3]))
				mat8000x200[i][j] = 1


#SlateBlue, MediumVioletRed, DarkOrchid,DeepSkyBlue,DarkRed,OrangeRed,Teal,
#Lime,DarkGoldenrod,PaleTurquoise,Plum,LightCoral,CadetBlue,DarkSeaGreen,PaleGoldenrod,RosyBrown
Cores = ['b', 'g', 'r', 'c','m','y', 'k', 'w', '#6A5ACD', '#C71585','#9932CC','#8B0000','#FF4500',
		'#008B8B','#00FF00','#B8860B','#E0FFFF','#DDA0DD' ,'#F08080' ,'#5F9EA0','#8FBC8F','#EEE8AA','#BC8F8F']


print "SVD"
U, s, V = LA.svd( mat8000x200 )

K = 3
SK =  np.diag(s)

#Normlizando a matriz S
Temp = SK/np.linalg.norm(SK)
SN = np.diag( Temp )

k = 0
#Salvando a matrix S.
print"Salvando a matriz S"
np.savetxt("S.txt", SK,fmt = '%.5f' ,delimiter = ';')

fig1 = plt.figure()
fig2 = plt.figure()
ax = fig1.add_subplot(111, projection='3d')

plt.axis([0, 20, 0, 1])
plt.plot(SN.T)
fig2.savefig('posto.png', dpi=200)


SK = SK[0:K,0:K]
Vaux = V.transpose()
VK = Vaux[:,:K]

aux = np.dot(SK , VK.transpose() )

print 'Gravando Matriz'
np.savetxt("Matriz1.txt", aux,fmt = '%.5f' ,delimiter = ';')

print "Geando grafico"

for i in range(len(DistribuicaFamiliasModelo)):
	if i == 0:
		x = aux[0:1,0:int(DistribuicaFamiliasModelo[i]) ];
		y = aux[1:2,0:int(DistribuicaFamiliasModelo[i]) ];
		z = aux[2:3,0:int(DistribuicaFamiliasModelo[i]) ];
	else:
		x = aux[0:1,int(DistribuicaFamiliasModelo[i-1]) +1 :int(DistribuicaFamiliasModelo[i])];
		y = aux[1:2,int(DistribuicaFamiliasModelo[i-1]) +1 :int(DistribuicaFamiliasModelo[i])];
		z = aux[2:3,int(DistribuicaFamiliasModelo[i-1]) +1 :int(DistribuicaFamiliasModelo[i])];
	ax.scatter(x, y, z, c=Cores[i], marker='o')

for i in range(len(DistribuicaFamiliasQuery)):
	if i == 0:
		x = aux[0:1,0:int(DistribuicaFamiliasQuery[i]) ];
		y = aux[1:2,0:int(DistribuicaFamiliasQuery[i]) ];
		z = aux[2:3,0:int(DistribuicaFamiliasQuery[i]) ];
	else:
		x = aux[0:1,int(DistribuicaFamiliasQuery[i-1]) +1 :int(DistribuicaFamiliasQuery[i])];
		y = aux[1:2,int(DistribuicaFamiliasQuery[i-1]) +1 :int(DistribuicaFamiliasQuery[i])];
		z = aux[2:3,int(DistribuicaFamiliasQuery[i-1]) +1 :int(DistribuicaFamiliasQuery[i])];
	ax.scatter(x, y, z, c=Cores[i+int(NumFamiliasModelo)], marker='^')

fig1.savefig('clus.png', dpi=200)
plt.close(fig1)

'''
x2 = aux[0:1,int(DistribuicaFamiliasModelo[0]) +1 :int(DistribuicaFamiliasModelo[1])];
y2 = aux[1:2,int(DistribuicaFamiliasModelo[0]) +1 :int(DistribuicaFamiliasModelo[1])];
z2 = aux[2:3,int(DistribuicaFamiliasModelo[0]) +1 :int(DistribuicaFamiliasModelo[1])];

x3 = aux[0:1,int(DistribuicaFamiliasModelo[1]) +1 :int(DistribuicaFamiliasModelo[2])];
y3 = aux[1:2,int(DistribuicaFamiliasModelo[1]) +1 :int(DistribuicaFamiliasModelo[2])];
z3 = aux[2:3,int(DistribuicaFamiliasModelo[1]) +1 :int(DistribuicaFamiliasModelo[2])];

'''


'''
x1 = aux[0:1,0:102];
x2 = aux[0:1,103:110];
x3 = aux[0:1,111:206];
x4 = aux[0:1,207:214];
x5 = aux[0:1,215:216];
y1 = aux[1:2,0:102];
y2 = aux[1:2,103:110];
y3 = aux[1:2,111:206];
y4 = aux[1:2,207:214];
y5 = aux[1:2,215:216];
z1 = aux[2:3,0:102];
z2 = aux[2:3,103:110];
z3 = aux[2:3,111:206];
z4 = aux[2:3,207:214];
z5 = aux[2:3,215:216];


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x1, y1, z1, c='b', marker='o')
ax.scatter(x2, y2, z2, c='g', marker='o')
ax.scatter(x3, y3, z3, c='r', marker='o')
ax.scatter(x4, y4, z4, c='k', marker='o')
ax.scatter(x5, y5, z5, c='y', marker='o')

plt.show()

'''

fim = time.time()
print "Tempo: ", fim-ini

Filemat.close()











