"""
Crie um dicionário para o cardápio e adicione um novo sabor com preço. 
Atualize o preço de um sabor existente e remova um sabor do cardápio.

"""

cardápio = {
    "margherita": 24.90,
    "portuguesa": 29.90,
    "4 queijos": 32.90,
}
print("💟 cardapio: ", cardápio)


cardápio["Romeu e julieta"] = 30.90
print("💌 cardapio atualizado: ", cardápio)

cardápio["portuguesa"] = 30.90
print("💚 cardapio atualizado: ", cardápio)

cardápio.pop("margherita")
print("💛 cardapio atualizado: ", cardápio)