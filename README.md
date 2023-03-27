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



