codigo = 10
salario = 1500.00
nome = 'Ronaldo'
situacao = True

tipo = type (salario)

# print(salario)
# print(tipo)
# Nesse caso, será exibido o tipo da variável de "salário", que é do tipo float.

# Formas de concatenação:
# print("Código: ", codigo, "| Nome: ", nome, "| O salário atual é de ", salario)

# Concatenação com "+" | Deve-se converter os valores que não são string para o tipo string (com "str)
print("Código: " + str(codigo) + "| Nome: " + nome + "| O salário atual é de " + str(salario))