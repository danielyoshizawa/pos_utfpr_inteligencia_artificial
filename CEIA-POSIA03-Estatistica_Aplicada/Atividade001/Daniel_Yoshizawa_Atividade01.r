### Atividade
# Implementar um script em linguagem R baseado no conjunto de
# dados USArrests, que deve calcular as médias das prisões por
# assaltos, assassinatos e estupros para as 5 maiores e as 5
# menores populações urbanas. Utilizar o conhecimento adquirido
# até o momento. Por exemplo, evitar funções de filtro e média.
# Identificar manualmente a quantidade de registros ou
# observações do conjunto de dados e realizar os demais cálculos
# via script.
###

# Atribuir a uma variavel o dataset
df <- USArrests

# Ordenar os elementos usando bubble sort (Row names não serão alterados pois ainda não foi ensinado na disciplina)
for (i in 1:(49)) { # Magic number :  length - 1, pode se usar a função nrows
  for (j in 1:(50 - i)) { # Magic number : obtido apartir da leitura do dataframe (50 linhas)
    if (df[j, ]$UrbanPop > df[j + 1, ]$UrbanPop) {
      temp <- df[j,]
      df[j,] <- df[j + 1,]
      df[j + 1,] <- temp
    }
  }
}

# Declarando variaveis
murderMenor <- 0
assaultMenor <- 0
rapeMenor <- 0
murderMaior <- 0
assaultMaior <- 0
rapeMaior <- 0


# Somar os 5 primeiros e os 5 ultimos valores
for (i in 1:5) {
  currBegin <- df[i, ]
  currEnd <- df[51-i,] # Magic number : Numero de linhas + 1, considerando que os indices em R começam em 1 e não em zero.
  murderMenor <- murderMenor + currBegin$Murder
  murderMaior <-  murderMaior + currEnd$Murder
  assaultMenor <- assaultMenor + currBegin$Assault 
  assaultMaior <- assaultMaior + currEnd$Assault
  rapeMenor <- rapeMenor + currBegin$Rape
  rapeMaior <- rapeMaior + currEnd$Rape
}

# Imprimir a media dos crimes
cat("Media de assassinatos nas 5 maiores cidades : " , murderMaior / 5)
cat("Media de assaultos nas 5 maiores cidades : " , assaultMaior / 5)
cat("Media de estupros nas 5 maiores cidades : " , rapeMaior / 5)
cat("Media de assassinatos nas 5 menores cidades : " , murderMenor / 5)
cat("Media de assaultos nas 5 menores cidades : " , assaultMenor / 5)
cat("Media de estupros nas 5 menores cidades : " , rapeMenor / 5)