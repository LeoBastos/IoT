import time
from urllib.parse import urljoin
import colorama
import requests
from requests.exceptions import HTTPError
from src.Model.sqlserver import insertSql
from src.config.conf import base_url
from src.func.ModuleEmail import send_mail


def get_urls():
    """Function para Buscar os modulos da Api"""

    print(colorama.Fore.CYAN + f':::::: Verificando API :::::', flush=True)

    tentativas = 0

    try:
        data = requests.get(urljoin(base_url, '6'))
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
        continue

    if tentativas == 3:
        send_mail(to_email=['email@.com'],
                  subject='Falha na Api', message=f'Erro ao retornar os modulos cadastrados na api!')
        print('email enviado')

    else:
        res = data.json()
        try:
            insertSql(res['Modulos'][0]['name'], res['Modulos'][0]['version'],
                      res['Modulos'][0]['url'], res['Modulos'][0]['isActive'])
            print(colorama.Fore.MAGENTA + f'Adicionando ao banco....')

        except:
            time.sleep(2)
            send_mail(to_email=['email@.com'],
                      subject="Erro Banco de Dados",
                      message=f'Erro ao persistir no banco')
            print('Ocorreu um erro ao tentar inserir no banco de dados')
