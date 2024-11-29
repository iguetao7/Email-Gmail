import smtplib
import email.message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os
from login import senha_app



def envia_email():
    msg = MIMEMultipart()
    #Assunto
    msg["Subject"] = 'E-mail enviado com python'
    #Remetente
    msg["From"] = 'EMAIL DE ENVIO'
    #Destino
    msg["To"] = 'EMAIL DE DESTINO'
    #Cópia
    msg["Cc"] = 'EMAIL DE DESTINO DA CÓPIA; EMAIL DE DESTINO DA CÓPIA'
    #Cópia oculta
    msg["Bcc"] = 'EMAIL DE DESTINO DA CÓPIA OCULPA'

    #Menssagem do email
    link_img = 'LINK DA IMAGEM'
    corpo_email = """<p>Boa tarde,</p>
    <p>Primeiro e-mail com python!</p>
    <img src='link_img'>"""

    #Anexando o corpo do email ao email
    msg.attach(MIMEText(corpo_email, 'html'))
    #Anexando arquivos
    lista_arquivos = os.listdir('anexos')
    for nome_arquivo in lista_arquivos:
        with open(f'anexos/{nome_arquivo}', 'rb') as arquivo:
            msg.attach(MIMEApplication(arquivo.read(), Name=nome_arquivo))

    #Conectando ao servidor do gmail
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    #Segurança cripptografada do email
    servidor.starttls()

    #Fazendo login
    servidor.login(msg['From'], senha_app)

    #Enviando a mensagem
    servidor.send_message(msg)

    #Fechando o login no servidor
    servidor.quit()
    print('E-mail enviado')

envia_email()
