import psutil
import datetime
from time import sleep
from datetime import datetime

# O metodo psutil.disk_io_counters() recupera as estatísticas atuais 
# de E/S do disco e as imprimimos no console
def teste_memoria():

    mem = psutil.virtual_memory()
    mem_total = mem.total / (1024*1024*1024) #memoria total em GB
    mem_available = mem.available / (1024*1024*1024) #memoria disponivel em GB
    mem_used = mem.used / (1024*1024*1024) #memoria usada em GB
    mem_percent = mem.percent #percentual de memoria usada

    data_atual = datetime.now().strftime('%d/%m/%Y')
    hora_atual = datetime.now().strftime('%H:%M')

    return mem_total, mem_available, mem_used, mem_percent, data_atual, hora_atual    

quantidade_testes = 10
intervalo_minutos = 1 
segundos = 60


for q in range(quantidade_testes):
    
    mem_total, mem_available, mem_used, mem_percent, data_atual, hora_atual = teste_memoria()   

    print('Teste {}/{} Data: {} Hora: {} | Total: {:.2f} GB | Disponivel: {:.2f} GB| Usada: {:.2f} GB | Percentual Usado: {:.2f} %'.format(q+1, quantidade_testes, data_atual, hora_atual, mem_total, mem_available, mem_used, mem_percent))    
    if (q+1) < quantidade_testes:
        sleep(intervalo_minutos*segundos)
        