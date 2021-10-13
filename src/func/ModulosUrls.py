import time
from urllib.parse import urljoin
import colorama
import requests
from requests.exceptions import HTTPError
from src.Model import ModelModulo
from src.config.conf import base_url
from src.func.ModuleEmail import send_mail


def get_urls():
    """Function para Buscar os modulos da Api"""

    print(colorama.Fore.CYAN + f':::::: Verificando API :::::', flush=True)

    tentativas = 0

    try:
        data = requests.get(urljoin(base_url, '1'))
        data.raise_for_status()
    except HTTPError as http_err:
        print(f'Erro de HTTP: {http_err}')
    except Exception as err:
        print(f'Outro erro ocorreu: {err}')
    else:
        print(f'Sucesso! {data.json()}')

    while data.status_code != 200 and tentativas < 3:
        print(f'Url: {data} - Tentativa: {tentativas}')
        tentativas += 1

    if tentativas == 3:
        send_mail(to_email=[''],
                  subject='Falha na Api', message=f'Erro ao retornar os modulos cadastrados na api!')
        print('email enviado')

    else:
        try:
            #ModelModulo.modulo.inserir(data['Modulos'][0]['name'], data['Modulos'][0]['version'],
            #                           data['Modulos'][0]['url'], data['Modulos'][0]['isActive'])
            print(colorama.Fore.MAGENTA + f'Adicionando ao banco....')
            time.sleep(1)

        except:
            time.sleep(2)
            send_mail(to_email=[''],
                      subject='Erro Banco de Dados: ' + data['Modulos'][0]['name'],
                      message=f'Erro ao persistir no banco: ' + data['Modulos'][0]['name'])
            print('Ocorreu um erro ao tentar inserir no banco de dados')







