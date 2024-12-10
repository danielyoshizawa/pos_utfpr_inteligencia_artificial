#Implemente a função aqui
def computeSum(*numbers):
    if not numbers:
        return "Nenhum valor recebido."
    return sum(numbers)

print(computeSum(10.0, 20.0, 30.0))
print(computeSum(5.0, 25.2))
print(computeSum(6.3, 50.3, 0, 29.4, 1205))
print(computeSum(5.1))
print(computeSum())