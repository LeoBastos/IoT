import json
import subprocess
import os
import time
from queue import Queue
from threading import Thread
import colorama
from src.config.conf import base_url, path
from requests import get
import psutil as ps
#
#
# def pingCliente(queue):
#     iplist = ['10.0.0.102', '10.0.0.118', '10.0.0.106']
#
#     with open(os.devnull, "wb") as limbo:
#         for ip in iplist:
#             result = subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip], stdout=limbo, stderr=limbo).wait()
#             with open(f'{path}/IP_Listagem.json', 'a') as outfile:
#                 json.dump(ip, outfile)
#
#             if result:
#                 with open(f'{path}/IP_inativos.json', 'a', encoding='utf-8') as outfile:
#                     json.dump(ip, outfile, separators=('', ' '))
#                 print(colorama.Fore.RED + f'IP Inativo: {ip}')
#
#
#
#
# def get_urls(queue):
#     print(colorama.Fore.CYAN + f'::: Registrando as Urls:', flush=True)
#     data = get(base_url).json()
#     with open(f'{path}/results.json', 'w', encoding='utf-8') as outfile:
#         json.dump(data, outfile, indent=2)
#         for cliente in data:
#             print(cliente)
#             queue.put(data)
#             time.sleep(1)
#         print(f':::  Tamanho da Queue: {queue.qsize()}')
#
#
# def checar_inativos(queue):
#         if queue.qsize() > 0:
#             queue.get()
#             with open(f'{path}/results.json', 'r') as j:
#                 json_data = json.load(j)
#                 for modulo in json_data:
#                     if not modulo['Modulos'][0]['isActive']:
#                         with open(f'{path}/URLS_inativo.json', 'w', encoding='utf-8') as outfile:
#                             json.dump(modulo, outfile, indent=2)
#                             print(colorama.Fore.BLUE + f'Clientes Inativos: {modulo}')
#                             time.sleep(1)
#                         queue.task_done()
#
#
# from verificaprocessos import VerificaProcesso
#
# program = VerificaProcesso([r"/home/leonardo/Área de Trabalho/exec/dist/filho/filho"])
#
# program.startProgram()
# input()
# program.stopProgram()

# print("ThreadMain Starting Process")
# process_name = "filho"
# pid = None
#
#
# for proc in ps.process_iter():
#     if process_name in proc.name() or 1 == 1:  # and proc.parent().as_dict(attrs=['name'])['name'] == 'sudo':
#         print('PID: [{}] (name: {})'.format(proc.pid, proc.name()))
#         print('PID: [{}] (parent: {})'.format(proc.pid, proc.parent()))
#         # print('PID: [{}] (children: {})'.format(proc.pid, proc.children(recursive=True)))
#         # print('PID: [{}] (cmdline: {})'.format(proc.pid, proc.cmdline()))
#         print('[----------------------------------------------]')
#         #proc.kill()
#

#Se estiver ativo, ele mata o processo
    # if 'filho' in proc.name():
    #     proc.kill()
    #     print('acabei')

#Se o processo n estiver ativo, ele executa o processo
# if not 'filho' in proc.name():
#      subprocess.Popen([r"/home/leonardo/Área de Trabalho/exec/dist/filho/filho"])
#      print('acabei')



#
# print("ThreadMain Finish Process")




# print('Lista de processos em execução:')
# for proc in ps.process_iter():
#     info = proc.as_dict(attrs=['pid', 'cmdline'])
#
#     with open(f'{path}/processos.json', 'w', encoding='utf-8') as outfile:
#         json.dump(info, outfile, indent=2)
#     print('Processo: {} - (path: {})'.format(info['pid'], info['cmdline']))
#
#     #Processo: 1 (PID: systemd)
#     #Processo: 39812(PID: python3.8)

#
#
# if __name__ == '__main__':
#     print(colorama.Fore.RED + f'Sistema Iniciado', flush=True)
#     queue = Queue()
#
#     th1 = Thread(target=get_urls, args=(queue,))
#     th2 = Thread(target=checar_inativos, args=(queue,))
#     th3 = Thread(target=pingCliente, args=(queue,))
#
#     th1.start()
#     th1.join()
#     th2.start()
#     th2.join()
#     th3.start()
#     th3.join()
#
#
#


# try:
#     data = get(urljoin(base_url, '2')).json()
#     print(data)
# except:
#     print('Teste de Exception quando api estiver off')