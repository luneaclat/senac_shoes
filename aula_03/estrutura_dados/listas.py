""" 
Homogênio -> Aceita apenas um tipo de dado
Heterogêneo -> Aceita dados de diferentes tipos
As estruturas de dados são declaradas com snake_case;
"""

# Declaração lista
# Ordenadas, mutáveis e heterogêneas

sabores = ["Mussarela", "calabresa","Frango com catupiry", "portuguesa"]
dados_pizza = ["Mussarela", 26.90, True]
# print("Sabores disponiveis: ", sabores)
# print("Informacoes da pizza: ", dados_pizza)


# Operações com listas
# 1. append() -> Adicionar um novo valor ao final da lista
sabores.append("margherita")
print("Sabores disponiveis: ", sabores)

# 2. remove() -> Remover um item da lista
sabores.remove("calabresa")
print("Sabores disponiveis: ", sabores)

# 3. Acessando os elementos da lista
pizzas = ["Mussarela", "calabresa","Frango com catupiry", "portuguesa"]
print("Primeiro sabor: ", pizzas[0])
print("Ultimo sabor: ", pizzas[-1])
# print("Todos os sabores: ", sabores[:])




























