import psutil
import speedtest as sp
from datetime import datetime
from time import sleep

def teste_internet():
    # Instanciando a função de test do Speedtest
    s = sp.Speedtest()
    s.get_servers()
    s.get_best_server()
    # Testando velocidades
    velocidade_download = round(s.download(threads=None)*(10**-6))
    velocidade_upload = round(s.upload(threads=None)*(10**-6))
    
    #Obtendo mais informaçoes da rede
    net_io_counters = psutil.net_io_counters()
    bytes_sent = net_io_counters.bytes_sent
    bytes_recv = net_io_counters.bytes_recv
    err_sent = net_io_counters.errout
    err_recv = net_io_counters.errin 

    # Capturando data e hora do teste
    data_atual = datetime.now().strftime('%d/%m/%Y')
    hora_atual = datetime.now().strftime('%H:%M')

    return data_atual, hora_atual, velocidade_download, velocidade_upload, bytes_sent, bytes_recv, err_sent, err_recv


quantidade_testes = 10
intervalo_minutos = 1 
# Loop para execução dos testes
for q in range(quantidade_testes):
    data_atual, hora_atual, velocidade_download, velocidade_upload, bytes_sent, bytes_recv, err_sent, err_recv = teste_internet()
    print('Teste {}/{} Data: {} Hora: {} | Download: {} MB/s | Upload: {} MB/s | Bytes Enviados Durante o Teste: {} | Bytes Recebidos Durante o Teste: {} | Total de Erros no Envio: {} | Total de Erros ao Receber: {}'.format(q+1, quantidade_testes, data_atual, hora_atual, velocidade_download, velocidade_upload, bytes_sent, bytes_recv, err_sent, err_recv))    
    if (q+1) < quantidade_testes:
       sleep(intervalo_minutos*60)