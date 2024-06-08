import threading
import time

num_processos = 5
token = [False] * num_processos
token[0] = True


def processo(processo_id):
    global token
    while True:
        if token[processo_id]:
            print(f"Processo {processo_id} entrou na seção crítica")
            time.sleep(1)
            print(f"Processo {processo_id} saiu da seção crítica")
            token[processo_id] = False
            token[(processo_id + 1) % num_processos] = True
        time.sleep(0.5)


threads = []
for i in range(num_processos):
    t = threading.Thread(target=processo, args=(i,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
