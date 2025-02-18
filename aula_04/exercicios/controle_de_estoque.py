"""
Crie um dicionário com os estoques de cada sabor. 
Decremente o estoque conforme os pedidos feitos e exiba uma mensagem se o estoque acabar.
"""
estoque = {
    "chocolate": 10,
    "baunilha": 8,
    "morango": 5,
    "limão": 7
}

estoques = {
    "mussarela": 10,
    "calabresa": 5,
    "frango com catupiry": 8,
    "portuguesa": 0,
    "4 queijos": 10,
    "margherita": 10,
    "Romeu e julieta": 0,
    
}

pedido = input("Informe seu pedido: ")

if pedido == "mussarela":
     estoques["mussarela"] -= 1
elif pedido == "calabresa":
    estoques["calabresa"] -= 1
elif pedido == "frango com catupiry":
     estoques["frango com catupiry"] -= 1
elif pedido == "portuguesa":
     estoques["portuguesa"] -= 1
elif pedido == "4 queijos":
     estoques["4 queijos"] -= 1
elif pedido == "margherita":     
     estoques["margherita"] -= 1
elif pedido == "Romeu e julieta":
     estoques["Romeu e julieta"] -= 1

for sabor, estoque in estoques.items():
    if estoque == 0:
        print(f"Estoque de {sabor} acabou!")
    else:
        print(f"Estoque de {sabor}: {estoque}")






        