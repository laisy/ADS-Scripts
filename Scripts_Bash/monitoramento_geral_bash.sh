#!/bin/bash

    echo Testes Data Hora CpuPercent QntCpus CpuTimesUser CpuTimesSystem CpuTimesIdle MemTotal MemAvaliable MemUsed DiskUsed DiskTotal DiskPercent BytesSend BytesRecv > monitoramento_bash_memoria.txt
    echo Testes Data Hora CpuPercent QntCpus CpuTimesUser CpuTimesSystem CpuTimesIdle MemTotal MemAvaliable MemUsed DiskUsed DiskTotal DiskPercent BytesSend BytesRecv
    
    num=1
    while [ $num -le 100 ]
    do
        data_atual=$(date +%Y/%m/%d)
        hora_atual=$(date +%H:%M:%S)

	#total de memoria ram
	mem=`free | grep  Mem | awk '{print $2}'`
	memoriaTotal=$(($mem/1024))

	#memoria livre
	memFree=`free | grep  Mem | awk '{print $4}'`
    	memoriaFree=$(($memFree/1024))

	#memoria em Uso
	memUso=`free | grep  Mem | awk '{print $3}'`
    	memoriaUsada=$(($memUso/1024))

	diskTotal=`df | grep /dev/nvme0n1p6 | awk '{print $2}'`
   	total=$diskTotal #converte os dados para GB
		
    	diskLivre=`df | grep /dev/nvme0n1p6 | awk '{print $4}'`
    	totalLivre=$diskLivre #converte os dados para GB

    	diskUsado=`df | grep /dev/nvme0n1p6 | awk '{print $3}'`
    	totalUsado=$diskUsado #converte os dados para GB
        
        diskTotal=`df | grep /dev/sda | awk '{print $2}'`
    	total=$diskTotal
		
    	diskPercent=`df | grep /dev/sda| awk '{print $5}'`
    	diskPercentUsed=$diskLivre

    	diskUsado=`df | grep /dev/sda | awk '{print $3}'`
    	totalUsado=$diskUsado
        	
    	qntCpus=`grep -c processor /proc/cpuinfo`
    	cpuPercent=`mpstat | grep all | awk '{print $3}'`
    	cpuTimesUser=`mpstat | grep all | awk '{print $4}'`
    	cpuTimesSystem=`mpstat | grep all | awk '{print $5}'`
    	cpuTimesIdle=`mpstat | grep all | awk '{print $12}'`
    	
    	transmit=0
	receive=0
	
	echo $num $data_atual $hora_atual $cpuPercent $qntCpus $cpuTimesUser $cpuTimesSystem $cpuTimesIdle $memoriaTotal $memoriaFree $memoriaUsada $totalUsado $total $diskPercentUsed $transmit $receive | tr "," . >> monitoramento_bash_memoria.txt
	echo $num $data_atual $hora_atual $cpuPercent $qntCpus $cpuTimesUser $cpuTimesSystem $cpuTimesIdle $memoriaTotal $memoriaFree $memoriaUsada $totalUsado $total $diskPercentUsed $transmit $receive | tr "," .
	
        sleep 3
        num=$(($num + 1))
    done
