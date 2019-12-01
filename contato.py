#biblioteca para usar o protocolo de envio de mensagens de correio eletrônico (smtp)
#biblioteca para organização da mensagem a ser enviado no modo de somente texto (MIMEText)
import smtplib
from email.mime.text import MIMEText

class EnviaEmail():
    """
    Esta classe tem por objetivo o envio de email

    ...

    Atributos
    ---------
    smtp_ssl_host : str
        Define que o protoloco de envio de mensagens de correio eletrônico (smtp), junto com o servidor do google(gmail)
    smtp_ssl_port : int
        define a porta de acesso
    username : str
        define o username(email) para logar no servidor
    password : str
        representa a senha do usuário para acessar o servidor
    from_addr : email
        email do usuário do sistema ao qual deseja manter contato 
    to_addrs : email 
        define o email ao qual receberá as mensegens enviada pelos usuários
    """
    def __init__(self, email):
        self.smtp_ssl_host = 'smtp.gmail.com'
        self.smtp_ssl_port = 465
        self.username = 'locafacil432@gmail.com'
        self.password = 'teste432*'
        self.from_addr = email
        self.to_addrs = ['locafacil432@gmail.com']

    def enviar(self, nome, mensagem):
        """
        Este método serve para enviar uma mensagem de um usuário do sistema para o email do servidor, estas mensagens são processados com o 
        MIMEText(somente texto)

        ...

        Parâmetros
        ----------
        nome : str
            nome do usuário do sistema ao qual deseja realizar contato
        mensagem : str
            mensagem que o mesmo deseja enviar
        """
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
