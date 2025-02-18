"""
Os conjuntos não são ordenados, são mutáveis, heterogêneos ou
homogêneos e não permitem elementos duplicados.
"""

#Declaração dos conjuntos
ingredientes = {"mussarela", "calabresa", "tomate", "azeitona"}
print("🍕 igredientes básicos: ", ingredientes)

# Operações com conjuntos
# Adicionar itens:
ingredientes.add("oregáno")
print("🧀 ingredientes atualizados: ", ingredientes)

# Remover itens:
ingredientes.remove("azeitona")
print("🧀 Ingredientes após a remoção: ", ingredientes)

# União de conjuntos:
adicionais = {"bacon", "palmito"}
todos_ingredientes = ingredientes.union(adicionais)
print("🧀 Todos os ingredientes: ", todos_ingredientes)

# Interseção de conjuntos: Aparecem em ambos os conjuntos
pizza_vegana = {"tomate", "azeitona","rúcula"}
comuns = ingredientes.intersection(pizza_vegana)
print("🧀 Ingredientes comuns: ", comuns)
