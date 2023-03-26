#!/bin/bash

# Exibe o uso atual da CPU
echo "Uso atual da CPU:"
top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1"%"}'

# Exibe o uso atual da memória 
echo "Uso atual da memória:"
free -h | grep Mem | awk '{print $3"/"$2 " ("$3/$2*100"%)"}'

# Exibe o uso atual do disco
echo "Uso atual do disco:"
df -h | awk '$NF=="/"{printf "%d/%dGB (%s)\n", $3,$2,$5}'

# Exibe o número de processos em execução
echo "Número de processos em execução:"
ps aux | wc -l

# Exibe a carga média do sistema
echo "Carga média do sistema:"
uptime | awk '{print $10,$11,$12}'
