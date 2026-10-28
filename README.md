# PDV com Descontos

## Sobre o projeto

Esse é um projeto de um sistema de vendas feito em Python para praticar o que estou aprendendo.

## Como funciona

O programa pede o preço do produto e a idade do cliente para calcular os descontos.

- Clientes com 65 anos ou mais recebem 20% de desconto.
- Se o valor depois desse desconto ficar acima de R$ 100,00, recebe mais 10% de desconto.
- Dá para registrar várias compras e digitar `0` no preço para encerrar.
- Se informar um preço ou uma idade negativa, o programa pede para digitar novamente.

No final, ele mostra a quantidade de compras, o valor total sem descontos, quanto foi descontado e o valor final das vendas.

Usei uma lista para guardar os dados das compras enquanto o programa está rodando.

## Como executar

Com o Python instalado, abra o terminal na pasta principal do projeto e execute:

```powershell
python .\nivel_1\pdv.py
```

## Alguns testes

| Preço | Idade | Valor final |
|---:|---:|---:|
| R$ 200,00 | 70 | R$ 144,00 |
| R$ 80,00 | 70 | R$ 64,00 |
| R$ 100,00 | 30 | R$ 100,00 |
| R$ 125,00 | 70 | R$ 100,00 |
| R$ 101,00 | 30 | R$ 90,90 |
