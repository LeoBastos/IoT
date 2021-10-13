import subprocess
import time
import psutil as ps


class ExecuteModule:
    """Classe para Iniciar ou Parar algum processo"""
    program = None

    def __init__(self, path):
        self.path = path

    def startModulo(self):
        try:
            self.program = subprocess.Popen(self.path)
            for proc in ps.process_iter():
                if 'filho' == proc.name():
                    print('PID: [{}] (name: {})'.format(proc.pid, proc.name()))
                    print('PID: [{}] (parent: {})'.format(proc.pid, proc.parent()))
                    time.sleep(2)
        except:
            print('Ocorreu um erro ao iniciar o processo do modulo')

    def stopModulo(self):
        try:
            time.sleep(5)
            #processName = self.program.name()
            for proc in ps.process_iter():
                if 'filho' in proc.name():
                    proc.kill()
                    print('FINALIZANDO PID: [{}] (name: {})'.format(proc.pid, proc.name()))
                    print('FINALIZANDO PID: [{}] (parent: {})'.format(proc.pid, proc.parent()))
        except:
            print('Ocorreu um erro ao Finalizar o processo do modulo')



