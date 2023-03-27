#!/bin/bash

echo Cont MemUsed MemFree MemShared Swap DiskUsed CpuUsr CpuSys CpuSoft CpuIdle Data Hora > log.txt
echo Cont MemUsed MemFree MemShared Swap DiskUsed CpuUsr CpuSys CpuSoft CpuIdle Data Hora

count=1

while [ True ]
do
	mem=`free | grep Mem | awk '{print $3, $4, $5, $6}'`
	swap=`free | grep Swap | awk '{print $3}'`
	disco=`df | grep footfs | awk '{print $3}'`
	cpu=`mpstat 1 1 | grep all | awk '{print $3, $5, $8, $12}'`
	data=`date --rfc-3339=seconds`

	echo $count $mem $swap $disco $cpu $data >> log.txt
	echo $count $men $swap $disco $cpu $data

	count=`expr $count + 1`

	sleep 2

done

