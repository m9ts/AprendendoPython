# Função para ler uma nota digitada pelo usuário
def lerNotas():
    n = float(input("Digite uma nota para o(a) aluno(a): "))
    return n  # Retorna a nota lida

# Função que calcula a média entre duas notas e exibe o resultado
def resultado(n1, n2):
    media = (n1 + n2) / 2

    print("Nota 1: ", n1)
    print("Nota 2: ", n2)

    print("Média: ", media, "\nResultado: ", end="")
    # O parâmetro end="" impede a quebra de linha que o print faz por padrão.
    # Assim, a próxima mensagem será impressa na mesma linha.

    if media >= 7:
        print("Aprovado!")
    else:
        print("Reprovado =/")

# Chamada da função lerNotas para capturar a primeira nota
a = lerNotas()

# Chamada da função lerNotas para capturar a segunda nota
b = lerNotas()

# Chamada da função resultado com as duas notas digitadas
resultado(a, b)
