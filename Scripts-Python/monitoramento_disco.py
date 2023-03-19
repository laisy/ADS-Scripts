import psutil
import datetime
from time import sleep
from datetime import datetime

# O metodo psutil.disk_io_counters() recupera as estatísticas atuais 
# de E/S do disco e as imprimimos no console
def teste_disco():
    disk_io_infos = psutil.disk_io_counters()

    # Calculando a velocidade de leitura em MB por Segundo
    disk_read_speed = (disk_io_infos.read_bytes / (1024*1024)) / (disk_io_infos.read_time / 1000)
    # Calculando a velocidade de escrita em MB por Segundo
    disk_write_speed = (disk_io_infos.write_bytes / (1024*1024)) / (disk_io_infos.write_time / 1000)

    # Obtendo mais informações do disco
    disk = psutil.disk_usage('/')
    disk_used = disk.used / (1024*1024*1024)
    disk_total = disk.total / (1024*1024*1024)
    disk_percent = disk.percent

    data_atual = datetime.now().strftime('%d/%m/%Y')
    hora_atual = datetime.now().strftime('%H:%M')

    return disk_read_speed, disk_write_speed, disk_used, disk_total, disk_percent, data_atual, hora_atual    

quantidade_testes = 10
intervalo_minutos = 1 
segundos = 60

for q in range(quantidade_testes):
    disk_read_speed, disk_write_speed, disk_used, disk_total, disk_percent, data_atual, hora_atual = teste_disco()   

    print('Teste {}/{} Data: {} Hora: {} | Leitura: {:.2f} MB/s | Escrita: {:.2f} MB/s | Disco Usado: {:.2f} GB | Disco Total: {:.2f} GB | Percentual Utilizado: {:.2f}%'.format(q+1, quantidade_testes, data_atual, hora_atual, disk_read_speed, disk_write_speed, disk_used, disk_total, disk_percent))    
    if (q+1) < quantidade_testes:
        sleep(intervalo_minutos*segundos)
        