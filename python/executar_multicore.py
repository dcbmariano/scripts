import os

cpus = 7

for i in range(cpus):
	os.system("nohup python simples.py 1000000000 &")

print('Executado em background com sucesso')