banknote = int(input("Digite o valor da cédula: "))
coin1 = int(input("Digite o valor de uma moeda: "))

while coin1 <= 0 or coin1 > 99:
  coin1 = int(input("Valor inválido. Digite o valor de uma moeda: "))

coin2 = int(input("Digite o valor da outra moeda: "))

while coin2 == coin1 or coin2 <= 0 or coin2 > 99:
  coin2 = int(input("Moeda inválida ou igual à primeira. Digite o valor da outra moeda: "))

coin1Print = coin1
coin1 = coin1 / 100
coin2Print = coin2
coin2 = coin2 / 100

if banknote % coin1 == 0 and banknote % coin2 == 0:
  print(f"Possível: {int(banknote // coin1)} moeda(s) de {coin1Print} ou {int(banknote // coin2)} moedas de {coin2Print}")
elif coin1 > coin2:
  if banknote % coin1 == 0:
    print(f"Possível: {int(banknote // coin1)} moeda(s) de {coin1Print} e 0 moedas de {coin2Print}")
  else:
    coin1Quantity = banknote // coin1
    if (banknote - (banknote % coin1)) % coin2:
      print(f"Possível: {int(coin1Quantity)} moeda(s) de {coin1Print} e {int((banknote - (banknote % coin1)) // coin2)} moedas de {coin2Print}")
    else:
      print("Não é possível fazer a troca.")
else:
  if banknote % coin2 == 0:
    print(f"Possível: 0 moeda(s) de {coin1Print} e {int(banknote // coin2)} moeda(s) de {coin2Print}")
  else:
    coin2Quantity = banknote // coin2
    if (banknote - (banknote % coin2)) % coin1:
      print(f"Possível: {int((banknote - (banknote % coin2)) // coin1)} moeda(s) de {coin1Print} e {int(coin2Quantity)} moeda(s) de {coin2Print}")
    else:
      print("Não é possível fazer a troca.")