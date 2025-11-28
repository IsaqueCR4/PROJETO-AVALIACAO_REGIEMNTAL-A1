# Contador de 1 a 100 com FOR exibindo apenas números pares
for numero in range(1, 101):
    if numero % 2 == 0:  # Verifica se o número é par
        print(numero)

# Contador de 1 a 100 com WHILE exibindo apenas números pares
numero = 1

while numero <= 100:
    if numero % 2 == 0:  # Verifica se o número é par
        print(numero)
    numero += 1

