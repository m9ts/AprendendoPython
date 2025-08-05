# Criação do arquivo
arquivo = open('arqText.txt', 'w')

# Escrita no arquivo anteriormente criado
arquivo.write('Curso Python \n')
arquivo.write('Aula prática')

# Fechamento do arquivo após escrita
arquivo.close()

# Leitura do arquivo
leitura = open('arqText.txt', 'r')
print(leitura.read())
leitura.close()

# Modo de abertura de arquivos em Python:
#
# r   -> Abre o arquivo somente para leitura.
#        O arquivo deve já existir.
#
# r+  -> Abre o arquivo para leitura e escrita.
#        O arquivo deve já existir.
#        A escrita começa na primeira linha e sobrescreve o conteúdo existente.
#
# w   -> Abre o arquivo somente para escrita, no início do arquivo.
#        Apaga o conteúdo existente. Cria o arquivo se não existir.
#
# w+  -> Abre o arquivo para escrita e leitura.
#        Apaga o conteúdo existente. Cria o arquivo se não existir.
#
# a   -> Abre o arquivo para escrita no final do arquivo.
#        Não apaga o conteúdo existente. Cria o arquivo se não existir.
#
# a+  -> Abre o arquivo para escrita no final do arquivo e leitura.
#        Não apaga o conteúdo existente. Cria o arquivo se não existir.
