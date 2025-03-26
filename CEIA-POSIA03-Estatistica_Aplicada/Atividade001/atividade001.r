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

# Imprimir as primeiras linhas do dataset
head(df)

# Atribuir a uma variavel o tamanho do dataset
numero_linhas <- nrow(df) # 50

# Ordenar os elementos usando bubble sort
for (i in 1:(numero_linhas - 1)) {
  for (j in 1:(numero_linhas - i)) {
    if (df[j, ]$UrbanPop > df[j + 1, ]$UrbanPop) {
      temp <- df[j,]
      df[j,] <- df[j + 1,]
      df[j + 1,] <- temp
    }
  }
}

# Unir o topo e o final
top_bottom_df <- rbind(head(df,5), tail(df,5))
print(top_bottom_df)

# Declarando variaveis
murder <- 0
assault <- 0
rape <- 0

# Calcular a soma dos valores por coluna
for (i in 1:nrow(top_bottom_df)) {
  curr <- top_bottom_df[i, ]
  murder <- murder + curr$Murder
  assault <- assault + curr$Assault
  rape <- rape + curr$Rape
}

# Calculando as medias
# Reutilizando as variaveis
murder <- murder / 10
assault <- assault / 10
rape <- rape / 10

# Imprimir a media dos crimes
cat("Media de assassinatos nas 5 maiores e 5 menores cidade : " , murder)
cat("Media de assaultos nas 5 maiores e 5 menores cidade : " , assault)
cat("Media de estupros nas 5 maiores e 5 menores cidade : " , rape)
