#!/bin/bash

while true
do
  # Obter o PID do processo desejado
  pid=$(pgrep -f "nome_do_processo")

  # Obter informações sobre o uso de memória do processo
  mem=$(ps -p $pid -o %mem | grep -v %MEM)

  # Exibir as informações de uso de memória
  echo "Uso de memória do processo: $mem"

  # Aguardar 1 segundo antes de executar novamente
  sleep 1
done