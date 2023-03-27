# ADS-Scripts
## Scripts Monitoramento Linux 
    1. Bash 
    2. Python 
    3. JavaScripts 
    
## Análise de Dados Python: 
    1. Pandas
    2. MatplotLib
    3. Numpy

## DADOS DE MONITORAMENTO 

    1. DISCO
    2. MEMÓRIA
    3. CPU
    4. REDE
    5. PROCESSOS

## SISTEMA DE CARGA

    1. JMeater
    2. Phoronix Test Suite
    3. STRESS-NG
## EXECUTAR SCRIPTS BASH

    sudo chmod a+x "nome_do_script".sh
    ./"nome_do_script".sh

## EXECUTAR SCRIPT PYTHON

    python3 "nome_do_script".py

## EXECUTAR SCRIPT JAVASCRIPT

    javac "nome_do_script".java

    Download do Sigar .JAR e todas as dependencias necessarias estao no link abaixo:
        https://sourceforge.net/projects/sigar/files/sigar/1.6/hyperic-sigar-1.6.4.zip/download
    Caso falte alguma DLL, inserir na pasta c:/Program Files/Java/jdk/bin

    1. Extraia o arquivo .zip
    2. Entre no diretório:
        cd hyperic-sigar-1.6.4
    3. sudo cp sigar-bin/lib/libsigar-amd64-linux.so /usr/lib/
    4. sudo cp sigar-bin/lib/sigar.jar /usr/share/java/

    5. Adicione o caminho do arquivo sigar.jar à variável de ambiente CLASSPATH. Você pode fazer isso adicionando a seguinte linha ao final do arquivo ~/.bashrc:
        export CLASSPATH=/usr/share/java/sigar.jar:$CLASSPATH

        1. Abra o arquivo .bashrc no editor de texto usando o comando:
            nano ~/.bashrc
        2. Role até o final do arquivo e adicione a seguinte linha:
            export CLASSPATH=/usr/share/java/sigar.jar:$CLASSPATH
        3. Pressione Ctrl+O para salvar as alterações e Ctrl+X para sair do editor de texto.
        4. Recarregue as variáveis de ambiente do seu shell com o seguinte comando:
            source ~/.bashrc ou . ~/.bashrc.

    6. Use cd Scripts_javaScript para entrar no diretório
    7. export CLASSPATH=/usr/share/java/sigar.jar:$CLASSPATH
    8. javac "nome_do_script".java

## JMEATER

    1. Download do JMeater em:
        https://jmeter.apache.org/download_jmeter.cgi
    2. Em Binaries, selecione:
        apache-jmeter-5.5.zip 	sha512 	pgp
    3. Extraia o arquivo .zip
    4. Acesse a pasta cd apache-jmeter-5.5/bin e abra o terminal
    5. Rode:
        ./jmeter

    OBS. JMeater é para testar a performance de aplicativos da web, serviços web, servidores FTP

## Phoronix Test Suite
    1. Download:
        https://www.phoronix-test-suite.com/.
    2. sudo dpkg -i Phoronix-Test-Suite.deb
    3. phoronix-test-suite list-tests
    4. phoronix-test-suite benchmark nome-do-teste

    MEMÓRIA:
        O teste "RAMspeed / SMP" é um conjunto de testes de benchmark de memória RAM que é executado com vários tipos diferentes de operações de memória, incluindo leitura, gravação e cópia. Ele também pode ser executado em sistemas com vários núcleos ou processadores, o que o torna uma boa opção para testar a memória em sistemas de alto desempenho.

        phoronix-test-suite benchmark ramspeed

    CPU:
        O teste "Timed Compilation" é um teste de benchmark que mede o tempo necessário para compilar um grande programa de software. Esse tipo de teste é útil para medir o desempenho da CPU em tarefas intensivas em CPU, como compilação de código ou renderização de vídeo.

        phoronix-test-suite benchmark timed-compilation

    DISCO:
        O teste "Disk Test" é um teste de benchmark que mede a velocidade de leitura e gravação do disco rígido ou unidade de estado sólido (SSD). Ele usa uma variedade de tamanhos de arquivos e padrões de acesso para testar a velocidade do disco em diferentes cenários de uso.

        phoronix-test-suite benchmark disk

    REDE:
        O teste "Disk Test" é um teste de benchmark que mede a velocidade de leitura e gravação do disco rígido ou unidade de estado sólido (SSD). Ele usa uma variedade de tamanhos de arquivos e padrões de acesso para testar a velocidade do disco em diferentes cenários de uso.

        phoronix-test-suite benchmark disk


## STRESS-NG

    1. sudo snap install stress-ng
    2. stress-ng --cpu 4 --io 2 --vm 1 --vm-bytes 512M --timeout 10s --metrics-brief
    3. stress-ng --cpu 4 
    4. stress-ng --vm 4 

## TESTE DE STRESS

    para criar um teste de estresse no disco rígido usando o "dd", você pode usar o seguinte comando:

        dd if=/dev/zero of=testfile bs=1G count=1 conv=fdatasync

    Para testar o desempenho da CPU, você pode usar o STRESS-NG para criar carga de trabalho na CPU:

        stress-ng --cpu 4 --timeout 60s
