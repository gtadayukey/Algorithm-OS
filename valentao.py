import random
import time


class Processo:
    def __init__(self, pid):
        self.pid = pid
        self.coordenador = None

    def enviar_mensagem(self, destino, mensagem):
        tempo_de_envio = random.uniform(0.1, 0.5)
        time.sleep(tempo_de_envio)
        destino.receber_mensagem(self, mensagem)

    def receber_mensagem(self, origem, mensagem):
        if mensagem == 'E':
            print(f"Processo {self.pid}: Recebi mensagem de eleição de {origem.pid}")
            self.enviar_mensagem(origem, 'PE')
            if origem.pid < self.pid:
                print(f"Processo {self.pid}: Sou o novo coordenador!")
                self.coordenador = self
                origem.atualizar_coordenador()
        elif mensagem == 'PE':
            print(f"Processo {self.pid}: Recebi mensagem para parar eleição de {origem.pid}")

    def atualizar_coordenador(self):
        self.coordenador = self


class Rede:
    def __init__(self, processos):
        self.processos = processos

    def eleger_coordenador(self):
        coordenador = random.choice(self.processos)
        print(f"Iniciando eleição... Processo {coordenador.pid} se candidata a coordenador.")
        for p in self.processos:
            if p != coordenador:
                p.enviar_mensagem(coordenador, 'E')
        time.sleep(1)

        for p in self.processos:
            if p.coordenador:
                return p

        return None


processos = [Processo(pid) for pid in range(1, 6)]
rede = Rede(processos)

coordenador = rede.eleger_coordenador()
if coordenador:
    print(f"Coordenador eleito: Processo {coordenador.pid}")
else:
    print("Não há coordenador!")
