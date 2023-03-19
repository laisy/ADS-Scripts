import psutil
import datetime
from time import sleep
from datetime import datetime

# O metodo psutil.disk_io_counters() recupera as estatísticas atuais 
# de E/S do disco e as imprimimos no console
def teste_cpu():

    cpu_percent = psutil.cpu_percent(interval=1) #utilizacao da CPU em porcentagem

    cpu_count = psutil.cpu_count(logical=True) #número de CPUs lógicas no sistema 
    
    cpu_times = psutil.cpu_times(percpu=False)
    cpu_times_user = cpu_times.user #tempo gasto por processos normais executando no modo de usuário
    cpu_times_system = cpu_times.system #tempo gasto pelos processos em execução no modo kernel
    cpu_times_idle = cpu_times.idle # tempo gasto ocioso        
    
    data_atual = datetime.now().strftime('%d/%m/%Y')
    hora_atual = datetime.now().strftime('%H:%M')

    return cpu_percent, cpu_count, cpu_times_user, cpu_times_system, cpu_times_idle, data_atual, hora_atual    

quantidade_testes = 10
intervalo_minutos = 1 
segundos = 60


for q in range(quantidade_testes):
    
    cpu_percent, cpu_count, cpu_times_user, cpu_times_system, cpu_times_idle, data_atual, hora_atual = teste_cpu()   

    print('Teste {}/{} Data: {} Hora: {} | Utilizado: {} % | Qnt CPUs no sistema: {} | Tempo gasto - processos normais no modo de usuario: {:.2f} s | Tempo gasto processos em execucao modo kernel: {:.2f} s | Tempo gasto ocioso: {:.2f} s'.format(q+1, quantidade_testes, data_atual, hora_atual, cpu_percent, cpu_count, cpu_times_user, cpu_times_system, cpu_times_idle))    
    if (q+1) < quantidade_testes:
        sleep(intervalo_minutos*segundos)
        