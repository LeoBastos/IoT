from os import makedirs
from os.path import exists


""" Configuração de Url """

base_url = f'http://127.0.0.1:8000/'


""" Configuração da IP list """

iplist = ['10.0.0.102', '10.0.0.106']


""" Configuração de Path """

path = '//home//leonardo//PycharmProjects//Projeto//src//logs'
path_modulo = [r"/home/leonardo/Área de Trabalho/exec/dist/filho/filho"]

if not exists(path):
    makedirs(path)


""" Configuração de Email """

# EMAIL_ADDRESS = ''
# EMAIL_PASSWORD = ''
# msg = EmailMessage()
# msg['Subject'] = 'Falha na Api'
# msg['from'] = 'leonardobastos04@gmail.com'
# msg['to'] = 'leonardo.bastos@criaresistemas.com'
# msg.set_content('Erro ao buscar valor da api')
#
# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#     smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#     smtp.send_message(msg)