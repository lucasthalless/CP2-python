string = input("Digite uma string: ")
invertedString = ""

# laço for que vai de 1 até a quantidade de caracteres da string mais um.
for x in range (1, len(string)+1):
  # adiciona o ultimo indice da string digitada pelo usuario menos o valor atual do contador do laço
  # de maneira que a variavel invertedString armazene a string invertida apos o fim do laço.
  # como o indice começa no zero, o contador precisa começar em um,
  # pois string[len(string)] esta uma posição na frente do ultimo indice da string
  invertedString += string[len(string)-x]

print(f"String invertida: {invertedString}")