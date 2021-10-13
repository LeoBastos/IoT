import os
import threading
import time
from datetime import datetime
import colorama
import schedule
from src.func.ModulosAtivos import VerificaModuloAtivo
from src.func.ModulosUrls import get_urls
from src.func.ModulosUpdate import updateModule

start_time = datetime.now().replace(microsecond=0)


def main():
    print(colorama.Fore.RED + f'Sistema Iniciado', flush=True)
    get_urls()
    updateModule()
    VerificaModuloAtivo()

    CPU_Pct = str(round(float(
        os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()),
        2))
    print(colorama.Fore.BLUE + "Uso de CPU = " + CPU_Pct)

    time_elapsed = datetime.now().replace(microsecond=0) - start_time
    print(time_elapsed)


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()
    job_thread.join()


schedule.every(120).seconds.do(main)

while 1:
    schedule.run_pending()
    time.sleep(1)
