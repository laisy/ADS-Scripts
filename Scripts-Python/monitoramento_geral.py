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
    
    return cpu_percent, cpu_count, cpu_times_user, cpu_times_system, cpu_times_idle    

# O metodo psutil.disk_io_counters() recupera as estatísticas atuais 
# de E/S do disco e as imprimimos no console
def teste_memoria():

    mem = psutil.virtual_memory()
    mem_total = mem.total / (1024*1024*1024) #memoria total em GB
    mem_available = mem.available / (1024*1024*1024) #memoria disponivel em GB
    mem_used = mem.used / (1024*1024*1024) #memoria usada em GB
    mem_percent = mem.percent #percentual de memoria usada

    return mem_total, mem_available, mem_used, mem_percent    

# O metodo psutil.disk_io_counters() recupera as estatísticas atuais 
# de E/S do disco e as imprimimos no console
def teste_disco():
    disk_io_infos = psutil.disk_io_counters()

    # Obtendo mais informações do disco
    disk = psutil.disk_usage('/')
    disk_used = disk.used / (1024*1024*1024)
    disk_total = disk.total / (1024*1024*1024)
    disk_percent = disk.percent


    return disk_used, disk_total, disk_percent    

def teste_rede():
    
    #Obtendo mais informaçoes da rede
    net_io_counters = psutil.net_io_counters()
    bytes_sent = net_io_counters.bytes_sent
    bytes_recv = net_io_counters.bytes_recv
    err_sent = net_io_counters.errout
    err_recv = net_io_counters.errin 

    # # Capturando data e hora do teste
    # data_atual = datetime.now().strftime('%d/%m/%Y')
    # hora_atual = datetime.now().strftime('%H:%M')

    return bytes_sent, bytes_recv, err_sent, err_recv

quantidade_testes = 200
intervalo_minutos = 1 
segundos = 1

#Escreve a label do arquivo
arquivo = open("monitoramento_py.txt", "w")
arquivo.write("Testes Data Hora CpuPercent QntCpus CpuTimesUser CpuTimesSystem CpuTimesIdle MemTotal MemAvaliable MemUsed DiskUsed DiskTotal DiskPercent BytesSend BytesRecv\n")
arquivo.close()

arquivo = open("monitoramento_py.txt", "a")
for q in range(quantidade_testes):
    
    cpu_percent, cpu_count, cpu_times_user, cpu_times_system, cpu_times_idle = teste_cpu()   
    mem_total, mem_available, mem_used, mem_percent = teste_memoria()   
    disk_used, disk_total, disk_percent = teste_disco()   
    bytes_sent, bytes_recv, err_sent, err_recv = teste_rede()

    data_atual = datetime.now().strftime('%Y/%m/%d')
    hora_atual = datetime.now().strftime('%H:%M:%S')
    print(data_atual)
    
    print('Teste {}/{} Data: {} | Hora: {} | CpuPercent: {} % | QntCpus: {} | CpuTimesUser: {:.2f} s | CpuTimesSystem: {:.2f} s | CpuTimesIdle: {:.2f} s | MemTotal: {:.2f} GB | MemAvaliable: {:.2f} GB| MemUsed: {:.2f} GB | DiskUsed: {:.2f} GB | DiskTotal: {:.2f} GB | DiskPercent: {:.2f}% | BytesSend: {} | BytesRecv: {}'.format(q+1, quantidade_testes, data_atual, hora_atual, cpu_percent, cpu_count, cpu_times_user, cpu_times_system, cpu_times_idle, mem_total, mem_available, mem_used, disk_used, disk_total, disk_percent, bytes_sent, bytes_recv))    

    arquivo.write("{} {} {} {:.2f} {:.2f} {:.2f} {:.2f} {:.2f} {:.2f} {:.2f} {:.2f} {:.2f} {} {} {}\n".format(q+1, data_atual, hora_atual, cpu_percent, cpu_count, cpu_times_user, cpu_times_system, cpu_times_idle, mem_total, mem_available, mem_used, disk_used, disk_total, disk_percent, bytes_sent, bytes_recv))
   
 
    if (q+1) < quantidade_testes:
        sleep(intervalo_minutos*segundos)
    
arquivo.close()