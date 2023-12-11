# Script:   paralelismo.py
# Objetivo: executa um script em paralelo por "n" vezes.
#           Enquanto houver núcleos de CPUs disponíveis
#           um novo processo será iniciado até que o
#           número total de vezes seja concluído.
# Autor:    Diego Mariano

import os  # usado para execução de programas externos
import psutil  # usado para contar as cpus
from time import time, sleep  # usado para pausar a busca por 10 seg
import multiprocessing as mp


def contaCPU():
    # returna o número de CPUs do computador

    tCPUs = 0
    try:
        tCPUs = psutil.cpu_count()
    except:
        tCPUs = psutil.NUM_CPUS

    return tCPUs

def temNucleoLivre(dados):
    # Retorna o id do primeiro core livre
    indice = -2

    try:
        indice = dados[:].index(False)
    except:
        indice = -1

    return indice


def executa(dados, id_nucleo, id_teste):
    # Funcao que executa o processo em paralelo
    print('-------------------------------')
    print("Executando o teste", id_teste, "no core", id_nucleo)
    print('[ ID do processo:', os.getpid(), '- Processo pai:', os.getppid(), ']')

    # Script externo que será executado
    os.system("python simples.py 100000000")

    dados[id_nucleo] = False
    print('[Processo Terminado]')


def main():
    # Principal função

    testes = 20

    procs = contaCPU()
    cont = 0 # contador para paralelizacao
    controle = [False]*procs  # define que todos os núcleos estão livres
    dados = mp.Array("i", controle)  # cria um array

    for i in range(testes):

        nucleo_livre = temNucleoLivre(dados)

        print('Teste:',i , '- Núcleo disponível:', nucleo_livre)

        # verifica se existe um núcleo livre
        if nucleo_livre >= 0:

            dados[nucleo_livre] = True  # indica que o núcleo está em uso

            # Excutando  *******************************
            p = mp.Process(target=executa, args=(dados, nucleo_livre, i)) 
            p.start()  # cria um novo processo
        
        # se não existir núcleo livre, aguarde
        else:
            while(nucleo_livre < 0):
                # Aguarde 10 seg e verifique novamente se o proc esta livre
                print('[ATENÇÃO: não há núcleos disponíveis]')
                print('Aguardando...')
                sleep(10)
                nucleo_livre = temNucleoLivre(dados)
            # executa para o item atual
            print('Repetindo teste:',i , '- Núcleo disponível:', nucleo_livre)
            dados[nucleo_livre] = True  
            p = mp.Process(target=executa, args=(dados, nucleo_livre, i)) 
            p.start()  

    p.join()  # requisitado para unir multiprocessos


# o script começará a ser executado por aqui         
if __name__ == '__main__':
    print('-------------------------------')
    print("main() iniciado.")
    print('-------------------------------')

    inicio = time()
    main()
    fim = time()

    print('-------------------------------')
    print("main() executado com sucesso em ", fim-inicio, "segundos")
    print('-------------------------------')
