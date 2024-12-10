def process_numbers():
    lista = []
    while True:
        i = int(input())
        if i == -1:
            break
        lista.append(i)

    print(f"A quantidade de números na lista: {len(lista)}")
    print(f"A soma dos números da lista: {sum(lista)}")
    print(f"A média considerando os valores na lista: {sum(lista) / len(lista)}")
    print(f"O maior número da lista: {max(lista)}")
    print(f"O menor número da lista: {min(lista)}")
    print(f"Quantos números da lista são maiores que a média: {sum(1 for i in lista if i > sum(lista) / len(lista))}")

if __name__ == "__main__":
    process_numbers()