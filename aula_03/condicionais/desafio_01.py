distancia = int(input("Informe a sua distância em km: "))


if distancia <= 5:
    frete = (5) + distancia
    print(f"O valor do frete é R$ {frete:.2f} 💳")
elif distancia > 5 and distancia <= 10:
    frete = (5) + distancia*2
    print(f"O valor do frete é R$ {frete:.2f} 💳")
else:
    print("Não entregamos nessa distância 😔❌")