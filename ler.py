from imap_tools import MailBox, AND
from login import senha_app


#Login
usuario ='SEU EMAIL'
senha = senha_app

meu_email = MailBox('imap.gmail.com').login(usuario, senha)

#Pastas disponíveis no email
# for pasta in meu_email.folder.list():
#   print(pasta)
#Pasta específica do email
# meu_email.folder.set('[Gmail]/E-mails enviados')

#Escolhendo os emails na caixa de entrada de acordo com remetente e destino
lista_email = meu_email.fetch(AND(from_='EMAIL DE ENVIO', to='EMAIL DE DESTINO'))
for i, email in enumerate(lista_email):
    if len(email.attachments) > 0:
        print(email.text)
        print(email.subject)
        print(email.html)
        for anexo in email.attachments:
            with open(f'Email {i + 1} - {anexo.filename}', 'wb') as arquivo:
                arquivo.write(anexo.payload)
            print('Anexo:', anexo.filename)
