# Sintaxe da estrutura For:
# - For {referência} in {sequência}: {bloco de código}

# Código para exibir números de 0 a 9, em ordem crescente:
for n in range(10):
    print(n)


# Detalhando o código:

# No exemplo que acabamos de ver, a variável n é inicialmente ajustada para 0 (inicialização com valor padrão).
# - Uma vez que n é menor do que 10 (condição), o comando print é executado.
# - Essa condição é adicionada com o comando range.
# - A variável n é incrementada em 1 (incremento padrão) e é testado se o valor de n ainda é menor do que 10.
# - O processo se repete até que o valor de n fique maior ou igual a 10.


# Alterando valor inicial:
for n in range(5, 16):
    print(n)


# Estrutura em ordem decrescente | Utilizando decremento no contador:
for n in range(10, 0, -1):
    print(n)