# sudo chmod a+x monitoramento_cpu.sh
# chmod +x monitoramento_cpu.sh
# ./monitoramento_cpu.sh

#!/bin/bash

#!/bin/bash

# Obter a saída do comando mpstat e filtrar apenas a linha de resumo da CPU
mpstat_output=$(mpstat -P ALL 1 1 | awk '/^Average:/ && $2 == "all" { print $0 }')

# Extrair o valor total de uso da CPU da linha de resumo
cpu_total=$(echo "$mpstat_output" | awk '{ printf "%.0f", 100 - $NF }')

# Imprimir o valor total de uso da CPU
echo "Valor total da CPU: $cpu_total%"

