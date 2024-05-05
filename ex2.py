num_de_produtos = int(input("quantos produtos você deseja saber o porcentual de aumento? "))

for i in range(num_de_produtos):
    preco_antigo = float(input("Digite o preço antigo do produto: "))
    preco_novo = float(input("Digite o preço novo do produto: "))
    porcentagem = (preco_novo - preco_antigo) / preco_antigo * 100
    print(f"O produto teve um aumento de {porcentagem:.2f}%")

