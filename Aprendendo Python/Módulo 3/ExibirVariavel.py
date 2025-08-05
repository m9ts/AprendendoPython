from operator import truediv

codigo = 105
nome = 'Jurumeu'
salario = 1650.00
ativo = True

 # Máscara | Tipo de Dado      | Descrição
 # --------|-------------------|-----------------------------------------------
 # %d / %i | int               | Exibe um valor inteiro.
 # %f      | float ou double   | Exibe um valor decimal.
 # %ld     | long int          | Exibe um número inteiro longo.
 # %e / %E | float ou double   | Exibe um número exponencial (científico).
 # %c      | char              | Exibe um caractere.
 # %o      | int               | Exibe um número inteiro em formato octal.
 # %x / %X | int               | Exibe um número inteiro em formato hexadecimal.
 # %s      | char              | Exibe uma cadeia de caracteres (string).
 # %r      | boolean           | Exibe True ou False (valor booleano).

# print("Código: %d" % codigo)
# print("Nome: %s " % nome)
# print("Salário: %.2f " % salario)
# print("Ativo: %r " % ativo)

# Ao utilizar input, a variável será considerada do tipo string.
# Para inserção de valores numéricos, deve-se converter o tipo de dado para o tipo que se deseja.

codigo = int(input("Digite o código do funcionário: "))
nome = input("Digite o nome do funcionário: ")
salario = float(input("Digite o salário do funcionário: "))
ativo = True

# Sequência   | Descrição
# ------------|---------------------------------------------------------------
# \n          | Insere uma quebra de linha.
# \t          | Insere tabulação horizontal.
# \v          | Insere tabulação vertical.
# \r          | Equivalente ao efeito da tecla Enter.
# \'          | Aspas simples.
# \"          | Aspas duplas.
# \\          | Insere uma barra invertida (backslash).
# \a          | Chamado de asc bell ou beep do sistema. Se houver suporte, aciona um bipe.
# \b          | Aciona o backspace, ou seja, apaga o caractere anterior.
# \f          | Insere uma quebra de página.
# \u          | Insere um caractere unicode. Deve acompanhar um código com 4 números.
