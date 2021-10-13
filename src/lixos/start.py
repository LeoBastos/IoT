# from src.Model import modulo
# from src.config.conf import EmailMessage, path_modulo
# from src.classes.ExecuteModules import ExecuteModule
# from src.config.conf import base_url
# import sqlite3
#
# import os
# import threading
# from datetime import datetime
# from urllib.parse import urljoin
# import colorama
# from requests import get
# import time
#
# start_time = datetime.now().replace(microsecond=0)
#
#
# def get_urls():
#     """Function para Buscar os modulos da Api"""
#     print(colorama.Fore.CYAN + f':::::: Verificando API :::::', flush=True)
#     tentativas = 0
#     data = get(urljoin(base_url, '2')).json()
#     print(data)
#     time.sleep(1)
#
#     while data == None and tentativas < 3:
#         print(f'Url: {data} - Tentativa: {tentativas}')
#         tentativas += 1
#
#     if tentativas == 3:
#         # EmailMessage()
#         print('email enviado')
#     else:
#         # modulo.ModuloDB.inserir(data['Modulos'][0]['idModulo'], data['Modulos'][0]['name'],
#         #                         data['Modulos'][0]['version'], data['Modulos'][0]['url'],
#         #                         data['Modulos'][0]['isActive'])
#         modulo.ModuloDB.listar('SELECT * FROM Modulo')
#         print(colorama.Fore.MAGENTA + f'Adicionando ao banco....')
#         time.sleep(1)
#
#         # print(data['Modulos'][0]['idModulo'], data['Modulos'][0]['name'],
#         #       data['Modulos'][0]['version'], data['Modulos'][0]['url'],
#         #       data['Modulos'][0]['isActive'])
#         # time.sleep(100)
#
#
# def updateModule():
#     """Verifica e executa a versão do Modulo caso esteja desatualizado"""
#     time.sleep(3)
#     print(colorama.Fore.LIGHTBLUE_EX + f'[-------------- Checando Versão do Modulo ----------------------]', flush=True)
#     data = get(urljoin(base_url, '1')).json()['Modulos'][0]['version']
#     print(f'Versão Atual...: {data} ')
#     time.sleep(2)
#
#     if data == 3:
#         print(f'Você já Possui a ultima Versão: {data} ')
#         time.sleep(2)
#     elif data == 2:
#         print(f'Versão Desatualizada {data}')
#         print('Verificar com PC como será o processo de update')
#         time.sleep(2)
#     else:
#         print(f'Versão Desatualizada {data}')
#         print('Verificar com PC como será o processo de update')
#         time.sleep(2)
#
#
# def VerificaModuloAtivo():
#     """ Function para Iniciar ou Parar o Processo/thread """
#     print(colorama.Fore.LIGHTMAGENTA_EX + '\n:::::: Inicializando Modulo :::::')
#
#     program = ExecuteModule(path_modulo)
#     program.startModulo()
#     time.sleep(12)
#
#     print('\n:::::: Finalizando Modulo ::::::')
#     program.stopModulo()
#
#
# if __name__ == '__main__':
#     print(colorama.Fore.RED + f'Sistema Iniciado', flush=True)
#
#     threads = [
#         threading.Thread(target=get_urls),
#         threading.Thread(target=updateModule),
#     ]
#
#     [th.start() for th in threads]
#     [th.join() for th in threads]
#
#     VerificaModuloAtivo()
#
#     time_elapsed = datetime.now().replace(microsecond=0) - start_time
#
#     CPU_Pct = str(round(float(
#         os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()),
#         2))
#     print(colorama.Fore.BLUE + "CPU Usage = " + CPU_Pct)
#
#
#     print('Fim Tempo total (hh:mm:ss) {}'.format(time_elapsed))
#
#
#     # #2 formas de pegar o processamento atual para possivel instrução
#     # print(psutil.cpu_percent())
#
#
