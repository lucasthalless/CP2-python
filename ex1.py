numQuantity = int(input("Informe a quatidade de numeros da sequencia: "))

# validar a quantidade de numeros (positivo)
while numQuantity <= 0:
  numQuantity = int(input("Quantidade inválida. Informe a quatidade de numeros da sequencia: "))

# quantidade de segmentos de numeros iguais consecutivos.
# começa como 1 pois o primeiro numero inputado já conta como um segmento.
equalNumsSegments = 1

# define as variaveis de numero atual e ultimo numero para utilizar no for.
currentNum = int(input("Informe um numero inteiro: "))
lastNum = currentNum

# laço que vai de 1 até a quantidade de números que devem ser inputados.
# começa no 1 e não no 0 pois o input do primeiro numero já aconteceu na linha 12.
for i in range(1, numQuantity):
  currentNum = int(input("Informe um numero inteiro: "))
  # se o numero atual for diferente do numero anterior, um novo segmento começa.
  if (currentNum != lastNum):
    equalNumsSegments = equalNumsSegments + 1
  # atualiza o numero anterior apos verificar o numero atual.
  lastNum = currentNum

print("{} foi a quantidade de segmentos de numeros iguais consecutivos.".format(equalNumsSegments))