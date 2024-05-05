num = int(input("Digite a quantidade de numeros da sequencia: "))
maior50 = 0
menor100 = 0
soma = 0

for i in range(num):
    seq = int(input("Digite um número da sequência: ")) 
    if seq > 50:
        soma += seq
    if seq < 100 :
        menor100 += 1

print(f"Soma de numeros maiores que 50: {soma}\nQuantidade de números menores que 100: {menor100}")
        