import time
from urllib.parse import urljoin
import colorama
from requests import get
from src.config.conf import base_url
from src.func.ModuleEmail import send_mail


def updateModule():
    """Verifica e executa a versão do Modulo caso esteja desatualizado"""
    time.sleep(3)
    print(colorama.Fore.LIGHTBLUE_EX + f'::::: Checando Versão do Modulo :::::]', flush=True)
    data = get(urljoin(base_url, '6')).json()['Modulos'][0]['version']
    print(f'Versão Atual...: {data} ')
    time.sleep(2)

    if data == 3:
        print(f'Você já Possui a ultima Versão: {data} ')
        time.sleep(2)
    else:
        send_mail(to_email=['*****@com'],
                  subject='Versão Desatualizada', message=f'Versão do IoT está desatualizado: {data}')
        print(f'A Versão atual está Desatualizada {data}')        
        time.sleep(2)

