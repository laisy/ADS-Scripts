
#recolher dados caso seja um ssd
diskSSD(){

	num=0

	while [ $num -lt 5 ]
	do

        	diskTotal=`df | grep /dev/nvme0n1p6 | awk '{print $2}'`
        	total=$(((diskTotal/1024)/1024)) #converte os dados para GB, idem para as outras variaveis
		
        	diskLivre=`df | grep /dev/nvme0n1p6 | awk '{print $4}'`
        	totalLivre=$(((diskLivre/1024)/1024))

        	diskUsado=`df | grep /dev/nvme0n1p6 | awk '{print $3}'`
        	totalUsado=$(((diskUsado/1024)/1024))
        	
        	echo $total $totalUsado $totalLivre >> monitoramentoDisco.txt
        	
		sleep 2
		num=$(($num+1))

	done


}

#recolher dados caso seja HD
diskHD(){

	num=0

	while [ $num -lt 5 ]
	do

        	diskTotal=`df | grep /dev/sda1 | awk '{print $2}'`
        	total=$(((diskTotal/1024)/1024))
		
        	diskLivre=`df | grep /dev/sda1| awk '{print $4}'`
        	totalLivre=$(((diskLivre/1024)/1024))

        	diskUsado=`df | grep /dev/sda1 | awk '{print $3}'`
        	totalUsado=$(((diskUsado/1024)/1024))
        	
        	echo $total $totalUsado $totalLivre >> monitoramentoDisco.txt
        	
		sleep 2
		num=$(($num+1))

	done


}

echo Total Usado Disponível > monitoramentoDisco.txt
diskSSD
