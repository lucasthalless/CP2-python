banknote = int(input("Digite o valor da cédula: "))
coin1 = int(input("Digite o valor de uma moeda: "))

# validar o valor da moeda (centavos)
while coin1 <= 0 or coin1 > 99:
  coin1 = int(input("Valor inválido. Digite o valor de uma moeda: "))

coin2 = int(input("Digite o valor da outra moeda: "))

# validar o valor da moeda (centavos) e se ela é igual à primeira moeda
while coin2 == coin1 or coin2 <= 0 or coin2 > 99:
  coin2 = int(input("Moeda inválida ou igual à primeira. Digite o valor da outra moeda: "))

# separar uma variável para mostrar a moeda para o usuário e outra para fazer operações
coin1Print = coin1
coin1 = coin1 / 100
coin2Print = coin2
coin2 = coin2 / 100

# se o resto da divisão do valor da cédula com cada uma das duas moedas for 0,
# apresenta duas formas possíveis de trocar a cédula em moedas
# (uma com cada moeda)
if banknote % coin1 == 0 and banknote % coin2 == 0:
  print(f"Possível: {int(banknote // coin1)} moeda(s) de {coin1Print} ou {int(banknote // coin2)} moedas de {coin2Print}")

# se a moeda 1 tiver um valor maior que a moeda 2
# fazer as operações priorizando a moeda 1,
# com intuito de facilitar o troco
# (maior valor = menos moedas).
elif coin1 > coin2:
  # tentar trocar apenas por moeda(s) 1, que possui um valor maior
  # e caso não seja possível, tentar incluir moeda(s) 2
  if banknote % coin1 == 0:
    print(f"Possível: {int(banknote // coin1)} moeda(s) de {coin1Print} e 0 moedas de {coin2Print}")
  else:
    coin1Quantity = banknote // coin1
    if (banknote - (banknote % coin1)) % coin2:
      print(f"Possível: {int(coin1Quantity)} moeda(s) de {coin1Print} e {int((banknote - (banknote % coin1)) // coin2)} moedas de {coin2Print}")
    else:
      print("Não é possível fazer a troca.")

# se a moeda 2 tiver um valor maior que a moeda 1
# fazer as operações priorizando a moeda 2,
# com intuito de facilitar o troco
# (maior valor = menos moedas)
else:
  # tentar trocar apenas por moeda(s) 2, que possui um valor maior
  # e caso não seja possível, tentar incluir moeda(s) 1
  if banknote % coin2 == 0:
    print(f"Possível: 0 moeda(s) de {coin1Print} e {int(banknote // coin2)} moeda(s) de {coin2Print}")
  else:
    coin2Quantity = banknote // coin2
    if (banknote - (banknote % coin2)) % coin1:
      print(f"Possível: {int((banknote - (banknote % coin2)) // coin1)} moeda(s) de {coin1Print} e {int(coin2Quantity)} moeda(s) de {coin2Print}")
    else:
      print("Não é possível fazer a troca.")