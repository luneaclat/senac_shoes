"""
Dado dois conjuntos de ingredientes, 
exiba os ingredientes comuns entre eles e 
os que estão disponíveis apenas em um conjunto.
"""

ingredientes = {"mussarela", "calabresa", "cebola", "oregano" }
veggie = {"palmito", "rúcula","oregano", "tomate", "azeitona", "cebola"}

ingredientes_comuns = ingredientes.intersection(veggie)
ingredientes_disponiveis = veggie.difference(ingredientes)
ingredientes_disponiveis2 = ingredientes.difference(veggie)

print("🧀 Ingredientes comuns: ", ingredientes_comuns)
print("🧀 Ingredientes disponíveis apenas em uma pizza vegana: ", ingredientes_disponiveis)
print("🧀 Ingredientes disponíveis apenas em uma pizza normal: ", ingredientes_disponiveis2)