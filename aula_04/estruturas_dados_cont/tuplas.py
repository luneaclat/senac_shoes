"""
As tuplas são coleções ordenadas, porém são imutáveis.
Homogêneas e podem ser heterogêneas
"""

tamanhos = ("pequena", "media", "grande")
print(f"""
    🌟 Tamanhos disponiveis: {tamanhos}
      """)

# Operações com tuplas
# Acessar ítens
print("🍕 Tamanho médio: ", tamanhos[1])

# Verificar itens
print("✅ existe tamanho grande? ", "grande" in tamanhos)

