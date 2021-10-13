import time
import colorama
from src.classes.ExecuteModules import ExecuteModule
from src.config.conf import path_modulo


def VerificaModuloAtivo():
    """ Function para Iniciar ou Parar o Processo/thread """
    print(colorama.Fore.LIGHTMAGENTA_EX + '\n:::::: Inicializando Modulo :::::')
    program = ExecuteModule(path_modulo)
    program.startModulo()

    time.sleep(5)

    print('\n:::::: Finalizando Modulo ::::::')
    program.stopModulo()
