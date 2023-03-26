#!/bin/bash

while true
do
  # Obter informações sobre todos os processos em execução
  processes=$(ps axo pid,pcpu,pmem,time,cmd)

  # Exibir as informações de uso de memória, uso de CPU e tempo de execução
  echo "PID  %CPU  %MEM  TIME  CMD"
  echo "$processes"

  # Aguardar 1 segundo antes de executar novamente
  sleep 1
done