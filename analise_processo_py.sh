#!/bin/bash

# Obter o nome do processo que será monitorado

  echo "DATA_ATUAL HORA_ATUAL PID  MEMTOTAL %CPU %MEM TIME MSECOND" > resultado_processo_py.txt 
  echo "DATA_ATUAL HORA_ATUAL PID  MEMTOTAL %CPU %MEM TIME MSECOND"

while true
do
  # Obter o ID do processo especificado
  pid=$(pgrep -f "python3 monitoramento_geral.py")
  
  if [ -n "$pid" ]; then
    # Obter informação de data e hora
    data_atual=$(date +"%Y-%m-%d %H:%M:%S")
    
    # Obter informações sobre o processo especificado
    process_info=$(ps -p $pid -o %cpu,%mem,time --no-headers)

    # Obter o tempo de execução em milisegundos
    elapsed_time=$(echo $process_info | awk -F: '{print ($1 * 3600 + $2 * 60 + $3) * 1000}')
      
    #calculo do script
    memTotal=`free | grep Mem | grep -v "grep" | awk '{print $2}'`
    #memPercent=$(ps -p $pid -o %mem | grep -v %MEM)
    #memConta=$(echo "$memTotal/100")
    #memUsed=$(echo "scale=2; $memConta * $memTotal" | bc -l)
    
    #echo $memUsed
          
    # Exibir as informações de uso de memória, uso de CPU e tempo de execução  
    echo "$data_atual $pid $memTotal $process_info $elapsed_time" >> resultado_processo_py.txt
    echo "$data_atual $pid $memTotal $process_info $elapsed_time"
       
  else
    # Se o processo não estiver em execução, exibir uma mensagem de aviso
    echo "Processo $pid não está em execução"
    break
  fi

  # Aguardar 1 segundo antes de executar novamente
  sleep 1
done
