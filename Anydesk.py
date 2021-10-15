import os.path
import subprocess
import sys
import time


path = '/usr/bin/anydesk'


def pingCliente():
    """Teste de Conectividade com a Internet"""
    print('\n::::: Teste de Conectividade :::::')
    with open(os.devnull, "wb") as limbo:
        for n in range(1, 3):
            ip = "anydesk.com"
            result = subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip], stdout=limbo, stderr=limbo).wait()
            if result:
                print(f'Sem internet')
            else:
                print(f'Pingando: {ip}, conectividade ok')

            time.sleep(3)


def verificaInstalacao(path):
    """Verifica se tem o AnyDesk instalado no path padrão"""

    print('\n::::: Verificando se Anydesk Existe na Máquina :::::')
    time.sleep(1)

    if os.path.exists(path):
        print('Anydesk está instalado')

    else:
        print('Anydesk não está instalado')
        time.sleep(2)

        print('Iniciando instalação')
        mypass = 'k4hvdc9g00leo'
        command = "apt install anydesk"
        os.system('echo %s|sudo -S %s' % (mypass, command))

    time.sleep(3)


def verificaServico():
    """Verificando status do Serviço"""

    print('\n::::: Verifica status do Serviço :::::')
    servico = os.system('anydesk --get-status')

    if servico == 0:
        print(f'\nServiço está Ativo')
    else:
        #os.system('anydesk --service') # iniciar o service
        #--restart-service #reiniciar o service
        print(f'\nServiço não está Ativo')


    time.sleep(3)


def pegarId():
    """Processo de Pegar o ID do AnyDesk"""
    print('\n:::::: Obtendo o ID de conexão do Anydesk ::::::')
    os.system('anydesk --get-id')
    time.sleep(3)


def openAnyDesk():
    try:
        null = open("/dev/null", "w")
        subprocess.Popen("anydesk", stdout=null, stderr=null)
        null.close()

    except OSError:
        print("AnyDesk com problemas")


if __name__ == '__main__':
    pingCliente()
    verificaInstalacao(path)
    verificaServico()
    pegarId()
    openAnyDesk()


