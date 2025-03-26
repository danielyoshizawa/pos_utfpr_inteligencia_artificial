import math

print(math.trunc(9.8))
print(math.ceil(5.6))
print(math.factorial(6))
print(math.floor(5.6))
print(abs(-185.2))
print(int(1.6))
print(divmod(3,2))

# 003 Complete as lacunas de modo a implementar um programa que coonta o numero de numeros impares
# e pares dada uma serie de numeros.

# Exemplo de entrada:
# (1,3,5,9,12,14,16,18,19,20,21)

# Saida esperada:
# Pares : 5
# Impares : 6

entrada = (1,3,5,9,12,14,16,18,19,20,21)

impares = 0
pares = 0

for n in entrada:
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Pares : {pares}")
print(f"Impares : {impares}")

# 004  Considere o código pré-implementado a seguir. 
# Implemente uma função chamada validaSenha que recebe uma string como argumento e verifica se os itens a seguir são atendidos. 
# Caso todos os itens forem atendidos, a função deve retornar True, senão False.

#     - Contenha no mínimo 5 caracteres e no máximo 15 caracteres;
#     - Contenha ao menos 2 números entre [0-9];
#     - No mínimo 2 caracteres em maiúsculo.

# Antes de enviar a resposta, sugiro testar o seu código com as seguintes senhas:
# Teste123 (Senha inválida)
# MinhaSenha123 (Senha válida)
# Minhasenha123 (Senha inválida)
# SS00 (Senha inválida)
# AS05939593jfjfkdfjdkfjkdjf (Senha inválida)
# czjf939 (Senha inválida)
# CS00 (Senha inválida)

import re

# Implementar a função validaSenha abaixo:
def validaSenha(password):
    if len(password) < 5 or len(password) > 15:
        return False
    if len(re.findall(r'[0-9]', password)) < 2:
        return False
    if len(re.findall(r'[A-Z]', password)) < 2:
        return False
    
    return True
 
#Não alterar o código abaixo
# myPass = input()

myPassList = ("Teste123", "MinhaSenha123", "Minhasenha123", "SS00", "AS05939593jfjfkdfjdkfjkdjf", "czjf939", "CS00")

for myPass in myPassList:
    if (validaSenha(myPass)):
        print("Senha válida")
    else:
        print("Senha inválida")
        
# 005 Complete as lacunas para implementar a função DictToList que deve receber um dicionário como parâmetro e retorna uma lista contendo os valores de cada chave do dicionário. Em seguida, utilize a função que realiza a soma de valores de um array da biblioteca Numpy.

import numpy as np

# # Implemente uma função retorne os valores das chaves de um dicionário em uma lista
def DictToList(dict):
    valores = list()

    for v in dict:
        valores.append(dict.get(v))

    return valores

faturamento = {
    "01/01/2023": 5500,
    "02/01/2023": 8850,
    "03/01/2023": 10500,
    "04/01/2023": 6000,
    "05/01/2023": 4500,
    "06/01/2023": 11000,
    "07/01/2023": 1260
}

lista_faturamento = DictToList(faturamento)

# Imprima a soma dos valores contidos em lista_faturamento usando uma função de soma do NumPy
print(np.sum(lista_faturamento))

# 006 Questão 1

# Preencha as lacunas a seguir considerando a manipulação de arquivos no Python.

# ----------- meuArquivo.txt -----------------
# id, nome_completo, sexo, renda_mensal, profissão
# 1, John Locks, M, 2500, Programador
# 2, Juma Lee, F, 3800, Analista
# 3, Stainer Silva, M, 5700, Analista Senior
# 4, Marina Young, F, 6300, Analista Senior
# 5, Zyon Lord, M, 1800, Suporte
# 6, Armindo Znah, 9500, Gerente de Projetos
# --------------------------------------------  

# #Implemente a leitura e impressão de todo o conteúdo do arquivo
arq = open("meuArquivo.txt", "r")
print(arq.read())

# Questão 2

# Preencha as lacunas de modo a armazenar a lista de vendas em um arquivo chamado "vendas.txt". 
# Caso o arquivo já exista, preserve o conteúdo do arquivo e adicione o novo conteúdo. 
# Cada linha do arquivo deve conter a data e o valor da venda conforme o exemplo a seguir:

# 05/02/2022, 1688.00,
# 08/02/2022, 2006.89,
# ...

vendas_list = [
    {
        "data": "05/02/2022",
        "valor": 1688.00,
    },
    {
        "data": "08/02/2022",
        "valor": 2006.89,
    },
    {
        "data": "09/02/2022",
        "valor": 1520.00,
    },
    {
        "data": "12/02/2022",
        "valor": 54.00,
    },
]

def gravarArquivo(vendas):
    arquivo = open('vendas.txt', 'a')

    for v in vendas:
        arquivo.write(f"\n{v['data']}, {v['valor']},")

		#Fechamento do arquivo
    arquivo.close()


gravarArquivo(vendas_list)

# 007 Preencha as lacunas de acordo com as instruções solicitadas nos comentários.

#1. Importe a biblioteca Pandas usando o alias "pd"
import pandas as pd

#2. Carregar dados a partir de um arquivo CSV em um dataframe a partir dos dados 
df = pd.read_csv('https://drive.google.com/uc?id=1AWPf-pJodJKeHsARQK_RHiNsE8fjPCVK&export=download')

#3. Imprimir os 10 primeiros registros do dataframe df
# print(df.head(10))

#4. Imprimir a última linha do dataframe df
print(df[-1:])

#5. Imprimir somente as linhas de índice par partindo do índice 2 (incluído) até 100 (excluído).
idxArray = range(2, 100, 2)

print(df.iloc[idxArray])

#6. Imprimir as colunas "First Name", "Last Name", "Email" e "Sex" cujo valor da coluna "Sex" seja "Female". 
print(df.loc[df['Sex'] == 'Female', ['First Name', 'Last Name', 'Email', 'Sex']])

#7. Excluir as colunas "User Id" e "Index" do dataframe "df"  
df.drop(columns=['User Id', 'Index'], inplace=True)

#8. Atribuir para um dataframe "new_df" os nomes das profissões (coluna "Job Title") e a quantidade de ocorrências de cada profissão do dataframe "df"
new_df = df.pivot_table(index=['Job Title'], aggfunc='size')

print(new_df)
