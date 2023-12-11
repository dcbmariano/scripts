import time
inicio = time.time()
import sys
entrada = int(sys.argv[1])
for i in range(0, entrada):
	dobro = i * 2
fim = time.time()
print('Terminado em', fim-inicio, 'segundos\n')
