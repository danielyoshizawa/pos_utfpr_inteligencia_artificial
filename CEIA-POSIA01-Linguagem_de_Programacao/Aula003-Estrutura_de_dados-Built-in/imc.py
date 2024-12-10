#Implemente a função a partir da linha de baixo
def computeIMC(n, p, a):
    return f"{n} tem {p} kg e {a} metros de altura. O seu IMC é {p / (a * a):.2f}"

try:
    n = input()
    p = float(input())
    a = float(input())
except ValueError:
    print("Não foi possível calcular o IMC.")
    exit(1)

print(computeIMC(n, p, a))
