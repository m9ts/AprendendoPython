# 📘 Manipulação de Arquivos Texto em Python

Por meio da linguagem Python, podemos manipular dados em um arquivo texto, mostrando as operações básicas de leitura e escrita.

Esse arquivo texto é conhecido como arquivo sequencial, porque a leitura tem de ser feita de forma sequencial, do início ao fim do arquivo.

Para trabalharmos com arquivos texto na linguagem Python utilizamos funções.


# Função open()

A função **open()** é utilizada para a abertura dos arquivos.

Sua sintaxe é:
**arquivo = open('arquivo.txt', 'w')**

A função open(), após a declaração da variável que receberá a função, necessita de dois parâmetros: primeiramente o nome do arquivo e, depois, o modo como estamos abrindo esse arquivo.

Na sintaxe apresentada acima foi utilizado o ‘w’ para fazer a escrita em um arquivo.

Caso o arquivo não exista nesse modo, o código criará um arquivo com o nome escrito no primeiro parâmetro.

**Observação:** Ao utilizar ‘w’ em um arquivo já existente, ele reescreverá todo o conteúdo do arquivo, fazendo com que todos os dados que estavam nele sejam apagados.


# Função write()

A função **write()** é utilizada para gravar informações em um arquivo existente.

Sua sintaxe é:
**arquivo.write('Curso Python')
arquivo.write('Aula prática')**

Na função, adicionamos o nome do arquivo e, logo após o símbolo do ponto final, fazemos a chamada da função **write**. Em seguida, adicionamos o texto que deverá ser gravado entre aspas simples.


# Função close()

A função **close()** é muito importante para encerrar o arquivo após sua utilização.

**Atenção:** Nunca abra o arquivo com a fun~]ap open e depois o faça de novo, sem antes fechar a instância anterior.

Sua sintaxe é:
**arquivo.close()**

Um dos motivos da necessidade da função close() é que se tentarmos escrever em um arquivo e não o fecharmos depois de terminar a escrita, as informações não chegarão ao arquivo e nada será escrito.


# Função read()

A função read() realiza a leitura de todo o conteúdo do arquivo.

Sua sintaxe é:
**leitura = open('arquivo.txt, 'r')
    print leitura.read()
        leitura.close()**

Utilizamos o parâmetro 'r' que representa que o arquivo está sendo aberto em modo leitura.
Desta forma, não é possível modificar os dados contidos no arquivo.

**Observação:** Ao utilizar a função **read()**, o nome do arquivo deve ser:
1) Uma string com o caminho completo (por exemplo, C Documentos teste txt)
2) O caminho em relação ao diretório atual (nomes txt do arquivo que se deseja abrir).

# Modo de abertura de arquivos em Python:

# r   -> Abre o arquivo somente para leitura.
        O arquivo deve já existir.

# r+  -> Abre o arquivo para leitura e escrita.
        O arquivo deve já existir.
        A escrita começa na primeira linha e sobrescreve o conteúdo existente.

# w   -> Abre o arquivo somente para escrita, no início do arquivo.
        Apaga o conteúdo existente. Cria o arquivo se não existir.

# w+  -> Abre o arquivo para escrita e leitura.
        Apaga o conteúdo existente. Cria o arquivo se não existir.

# a   -> Abre o arquivo para escrita no final do arquivo.
        Não apaga o conteúdo existente. Cria o arquivo se não existir.

# a+  -> Abre o arquivo para escrita no final do arquivo e leitura.
        Não apaga o conteúdo existente. Cria o arquivo se não existir.
