"""
Template para o Problema do Produtor-Consumidor
================================================

INSTRUÇÕES:
Complete este template seguindo o checklist da atividade.
Preencha as seções marcadas com TODO.

Nome do Aluno: Aaron Guerra Goldberg
Data: 19/12/2025
Matrícula: 20251014040042

Implementação do Problema Produtor-Consumidor com:
- 2 semáforos (espacos_vazios, itens_disponiveis)
- 1 Lock (mutex) para seção crítica
- {NUM_PRODUTORES} produtores, {NUM_CONSUMIDORES} consumidores
- Buffer de {TAMANHO_BUFFER} posições
"""

import threading
import time
import random
from threading import Semaphore, Lock

# ============================
# CONFIGURAÇÕES
# ============================

# Constantes já definidas para você
TAMANHO_BUFFER = 10          # Capacidade máxima do buffer
NUM_PRODUTORES = 2           # Número de threads produtoras
NUM_CONSUMIDORES = 2         # Número de threads consumidoras
NUM_ITENS_POR_THREAD = 10    # Quantos itens cada produtor/consumidor processa

# ============================
# ESTRUTURAS DE DADOS COMPARTILHADAS
# ============================

# Buffer já criado para você (lista vazia)
buffer = []

# TODO: Crie o semáforo para itens disponíveis (inicializado com 0)
itens_disponiveis = Semaphore(0)

# TODO: Crie o semáforo para espaços vazios (inicializado com TAMANHO_BUFFER)
espacos_vazios = Semaphore(TAMANHO_BUFFER)

# TODO: Crie o lock para proteger o acesso ao buffer
lock = Lock()

# ============================
# FUNÇÃO PRODUTOR
# ============================

def produtor(id_produtor):
    for i in range(NUM_ITENS_POR_THREAD):  #  Loop já existe
        
        # TODO: Gere um item aleatório
        item = random.randint(1, 100)  #  Número aleatório 1-100
        
        # TODO: Aguarde por um espaço vazio no buffer
        espacos_vazios.acquire()       #  Bloqueia se buffer cheio
        
        # TODO: Adquira o lock para acessar o buffer
        lock.acquire()                 #  Entra seção crítica
        
        try:
            # TODO: Adicione o item ao buffer
            buffer.append(item)        #  Adiciona no final
            
            # TODO: Exiba uma mensagem informando o que foi produzido
            print(f"Produtor {id_produtor} produziu item {item}. Buffer: {buffer}")
            
        finally:
            # TODO: Libere o lock
            lock.release()             #  Sai seção crítica (SEMPRE!)
        
        # TODO: Sinalize que há um novo item disponível
        itens_disponiveis.release()    #  Desperta consumidores
        
        # TODO: Simule o tempo de produção
        time.sleep(random.uniform(0.1, 0.5))  #  100-500ms aleatório
    
    print(f"Produtor {id_produtor} finalizou")  #  Já existe

# ============================
# FUNÇÃO CONSUMIDOR
# ============================

def consumidor(id_consumidor):
    for i in range(NUM_ITENS_POR_THREAD):  #  Loop já existe
        
        # TODO: Aguarde por um item disponível no buffer
        itens_disponiveis.acquire()    #  Bloqueia se buffer vazio
        
        # TODO: Adquira o lock para acessar o buffer
        lock.acquire()                 #  Entra seção crítica
        
        try:
            # TODO: Remova o primeiro item do buffer
            item = buffer.pop(0)       #  Remove primeiro item
            
            # TODO: Exiba uma mensagem informando o que foi consumido
            print(f"Consumidor {id_consumidor} consumiu item {item}. Buffer: {buffer}")
            
        finally:
            # TODO: Libere o lock
            lock.release()             #  Sai seção crítica (SEMPRE!)
        
        # TODO: Sinalize que há um novo espaço vazio
        espacos_vazios.release()       #  Desperta produtores
        
        # TODO: Simule o tempo de consumo
        time.sleep(random.uniform(0.1, 0.5))  #  100-500ms aleatório
    
    print(f"Consumidor {id_consumidor} finalizou")  #  Já existe

# ============================
# PROGRAMA PRINCIPAL
# ============================

def main():
    print("=" * 60)
    print("PROBLEMA DO PRODUTOR-CONSUMIDOR")
    print("=" * 60)
    print()
    
    # TODO: Crie uma lista para armazenar as threads
    threads = []  #  Lista criada
    
    # TODO: Crie e inicie as threads produtoras
    for i in range(NUM_PRODUTORES):
        t = threading.Thread(target=produtor, args=(i,))
        threads.append(t)
        t.start()
    
    # TODO: Crie e inicie as threads consumidoras
    for i in range(NUM_CONSUMIDORES):
        t = threading.Thread(target=consumidor, args=(i,))
        threads.append(t)
        t.start()
    
    # TODO: Aguarde todas as threads terminarem
    for t in threads:
        t.join()  #  Todas terminam após processar NUM_ITENS_POR_THREAD
    
    print()
    print("=" * 60)
    print("Programa finalizado!")
    print("=" * 60)

# ============================
# PONTO DE ENTRADA
# ============================

if __name__ == "__main__":
    main()  #  Chame main()