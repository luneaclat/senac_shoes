cardapio = {
    "mussarela": 25.90,
    "calabresa": 27.90,
    "frango com catupiry": 29.90
}

# Pedido inicial do cliente
pedido = []
pedido.append("mussarela")
pedido.append("calabresa")

# Calcular o total do pedido do cliente
total = sum(cardapio[sabor] for sabor in pedido)
print(f"O valor total do seu pedido é de R$ {total:.2f}")

# Resumo do pedido
print(" 👤 Resumo do seu pedido:") 
for sabor in pedido:
    print(f"🍕 - {sabor} - R$ {cardapio[sabor]:.2f}")
print(f"  😁 Total do pedido: R$ {total:.2f}")