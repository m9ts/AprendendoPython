notaA = float(input("Informe a primeira nota: "))
notaB = float(input("Informe a segunda nota: "))

# Calcular média:
mediaFinal = (notaA + notaB) / 2

# Verificação:
if mediaFinal >= 7.0:
    print("A média foi de: %.1f - Aprovado" % mediaFinal)
else:
    print("A média foi de: %.1f - Reprovado" % mediaFinal)