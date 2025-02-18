"""
Os dicionários podem ser heterogênios ou homogêneos
São ordenados, mutáveis, e sempre são acompanhados por uma chave:valor
"""

# Declaração de um dicionário
cardápio = {
    "mussarela": 25.90,
    "calabresa": 27.90,
    "frango com catupiry": 29.90
}

print("💌 cardápio da pizzaria sabores ", cardápio)

# Operações com dicionários
# 1. Acessar valores:
print("💟 Preço da pizza de calabresa: R$", cardápio["calabresa"])

# 2. Adicionar itens:
cardápio["portuguesa"] = 30.90
print("💟 cardapio atualizado: ", cardápio)

# 3. Alterar valores:
cardápio["mussarela"] = 26.90
print("💟 Preço atualizado da pizza de mussarela: R$", cardápio["mussarela"])

# 4. Iterar sobre o dicionário:
for sabor, preco in cardápio.items():
    print(f"\n👤 A pizza de {sabor} custa R$ {preco} ") 