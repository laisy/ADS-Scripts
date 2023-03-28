#!/bin/bash

# Ler o arquivo /proc/stat para obter informações de uso da CPU
cpu_info=$(cat /proc/stat | grep 'cpu ')

# Definir o separador de campo como espaço
IFS=' '

# Ler as informações de uso da CPU em variáveis separadas
read cpu _ user nice system idle iowait irq softirq steal guest guest_nice << $cpu_info

# Calcular o valor total de uso da CPU
cpu_total=$((user+system+nice+idle+iowait+irq+softirq+steal+guest+guest_nice))

# Imprimir o valor total de uso da CPU
echo "Valor total da CPU: $cpu_total"
