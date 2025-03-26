## Parte 001
#Fator
vetor <- c(10,20,10,30,40)
summary(vetor)

is.numeric(vetor)

vetor <- as.factor(vetor)
summary(vetor)

is.numeric(vetor)

#Filtro
vogais <- c("a", "e", "i", "o", "u")
vogais[-3]

vogais[vogais == "o"]
vogais[vogais == "g"]

#Funções
fatorial <- function(numero) {
  i <- 1
  multiplicacao <- 1
  while(i <= numero) {
    multiplicacao <- multiplicacao * i
    i <- i + 1
  }
  
  return(multiplicacao)
}

fatorial(5)

# Fora do escopo
# multiplicacao

# Lista e dataframes permitem armazenar valores heterogeneos

nome <- c("Joao", "Maria", "Jose", "Rafael")
idade <- c(30,20,25,31)

df <- data.frame(nome, idade)

summary(df)
df$nome[df$idade >= 30]

df$nome[1] # Primeiro nome
df$idade[1] # Primeira idade
df[1,] # Primeira Linha
df[1:3,] # Tres primeiras linhas
df[,1] # Primeira coluna

df$nova <- NA # Adicionar nova coluna com valores nulos
df$nova <- NULL # Deletar linha

# Ler arquivo
setwd("/home/daniel/Development/PosUtfprInteligenciaArtificial/CEIA-POSIA03-Estatistica_Aplicada/Aula002") #Define diretorioo
df <- read.csv("clima.csv")

## Parte 002
vetor <- c(10,19,10,20,30,40)
summary(vetor) # Informa informações sobre o vetor

## Medidas de localização
# Calculo da media
mean(vetor) # Soma todos os elementos e divide pelo numero de elementos
# Calculo da media usando um dataframe
mean(mtcars$hp)
# Calcular a mediana
# Elementos são ordenados e verifica qual o elemento central
# Caso o numero de elementos seja par, é feita a media dos elementos
# centrais
median(vetor)
# Mediana de dataframe
median(USArrests$Murder)

## Medidas de dispersão
# Variancia - Soma das distancias entre o valor e a media elevado ao quadrado dividido por N ou N-1
# Divide por N para variação populacional
# Divide por N-1 para amostragem populacional
#
# sum(valor - mean)^2 / (N ou N-1)
#
# A variancia ajuda a entender oo quão "espalhados" os dados estão
var(vetor) # Calcula a variancia amostral

# Desvio padrão
# Raiz quadrada da variancia
# O desvio padrão é uma medida prática para entenderr a dispersão dos dados.
# Ele complementa a variancia, mas é mais facil de interpretar porque
# está na mesma unidade dos dados. Por exemplo, se os dados estão em
# metros, o desvio padrão também estará em metros.
#
# Desvio padrão pequenoo: os dados estão proximos da media
# Desvio padrão grande : os dados estão mais espalhados
sd(vetor)
