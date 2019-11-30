import smtplib
from email.mime.text import MIMEText

class EnviaEmail():
    def __init__(self, email):
        # conexão com os servidores do google
        self.smtp_ssl_host = 'smtp.gmail.com'
        self.smtp_ssl_port = 465
        # username ou email para logar no servidor
        self.username = 'locafacil432@gmail.com'
        self.password = 'teste432*'
        self.from_addr = email
        self.to_addrs = ['locafacil432@gmail.com']

    def enviar(self, nome, mensagem):
        # a biblioteca email possuí vários templates
        # para diferentes formatos de mensagem
        # neste caso usaremos MIMEText para enviar
        # somente texto
        message = MIMEText(nome)
        message['subject'] = str(mensagem) + ' ' + str(self.from_addr)
        message['from'] = self.from_addr
        message['to'] = ', '.join(self.to_addrs)
        # conectaremos de forma segura usando SSL
        server = smtplib.SMTP_SSL(self.smtp_ssl_host, self.smtp_ssl_port)
        # para interagir com um servidor externo precisaremos
        # fazer login nele
        server.login(self.username, self.password)
        server.sendmail(self.from_addr, self.to_addrs, message.as_string())
        server.quit()
