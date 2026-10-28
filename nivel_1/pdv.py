print ("===SISTEMA DE VENDAS PDV====")

# Armazena em lista os dados de cada compra.
compras = []

# Entrada de dados do usuário.
preco = float(input("Valor produto?: "))
while preco < 0:
    print("Valor invalido, passar novamente!")
    preco = float(input("Valor do produto?"))

while preco != 0:
    idade = int(input("Qual a idade?: "))
    while idade < 0:
        print("Valor invalido, passar novamente!")
        idade = int(input("Qual a idade?"))

    precoFinal = preco
    descontoTotal = 0

    # Aplica o desconto por idade.
    if idade >= 65:
        desconto = preco * 20 / 100
        precoFinal = preco - desconto
        descontoTotal = descontoTotal + desconto
        print('Cliente tem direito ao desconto!')

    # Aplica desconto adicional se o preço passar de R$ 100.
    if precoFinal > 100:
        desconto = precoFinal*10/100
        precoFinal = precoFinal - desconto
        descontoTotal = descontoTotal + desconto

    print('\n===VALOR===')
    print(f"Valor final do produto: R$ {precoFinal:.2f}")
    compras.append([preco, descontoTotal, precoFinal])

    preco = float(input("Valor do próximo produto (0 para encerrar): "))

    while preco < 0:
        print("Valor invalido, passar novamente!")
        preco = float(input("Valor do produto (0 para encerrar): "))

quantidadeCompras = len(compras)
print("\n===RESULTADO===")
print("Quantidade de compras:", quantidadeCompras)

totalBruto = 0
for compra in compras:
    totalBruto = totalBruto + compra[0]
print(f"Total bruto: R$ {totalBruto:.2f}")

totalDescontos = 0
for compra in compras:
    totalDescontos = totalDescontos + compra[1]
print(f"Total de descontos: R$ {totalDescontos:.2f}")

totalFinal = 0
for compra in compras:
    totalFinal = totalFinal + compra[2]
print(f"Total final das vendas: R$ {totalFinal:.2f}")