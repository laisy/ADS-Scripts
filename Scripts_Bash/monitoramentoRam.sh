# Função para executar cada calcular o número de execuções de cada programa
memoriaRam(){

	num=0

	while [ $num -lt 5 ]
	do

		#total de memoria ram
		mem=`free | grep  Mem | awk '{print $2}'`
		memoriaTotal=$(($mem/1024))

		#memoria livre
		memFree=`free | grep  Mem | awk '{print $4}'`
        memoriaFree=$(($memFree/1024))

		#memoria em Uso
		memUso=`free | grep  Mem | awk '{print $3}'`
        memoriaUsada=$(($memUso/1024))

		#memoria em buff/cache
		memBC=`free | grep  Mem | awk '{print $6}'`
        memoriaBC=$(($memBC/1024))

		#porcentagem de memoria usada
		porcentagem=$((($memUso*100)/$mem))

		echo $memoriaTotal $memoriaUsada $memoriaFree $memoriaBC $porcentagem >> monitoramentoRam.txt
		sleep 2
		num=$(($num+1))

	done


}

echo total used free buff/cache porcentagem > monitoramentoRam.txt
memoriaRam