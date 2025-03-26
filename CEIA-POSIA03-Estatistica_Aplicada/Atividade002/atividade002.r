# Atividades
# - Implementar um script usando a linguagem R para calcular a moda em
# relação ao número de cilindros do mtcars
# - Implementar um script usando a linguagem R para calcular por meio
# de uma função a variância populacional para o número de prisões por
# assaltos do USArrests
# - Implementar um script em linguagem R para calcular a média, a
# mediana, a variância e o desvio-padrão das populações das linhas
# pares do USArrests

# 01 - Cacular a moda em relação ao numero de cilindros
frequencia_cilindros <-  table(mtcars$cyl)
moda <- as.numeric(names(frequencia_cilindros)[frequencia_cilindros == max(frequencia_cilindros)])
print(moda)

# 02 - Variancia populacional para o numero de prisões por assaltos
var_populacional <- function(populacao) {
  n <- length(populacao)
  media <- mean(populacao)
  soma_quadrados <- sum((populacao - media)^2)
  variancia_populacional <- soma_quadrados / n
  return(variancia_populacional)
}

# Variancia amostral para o numero de prisões por assalto
var(USArrests$Assault)

# Variancia populacional para o numemro de prisões por assalto
var_populacional(USArrests$Assault)

# 03 - Calcular a media, mediana, varianca e o desvio-padrao das
# populacoes das linhas pares
indices_pares <- seq(from = 2, to = nrow(USArrests), by=2)
linhas_pares <- USArrests[indices_pares,]
mean(linhas_pares$UrbanPop)
median(linhas_pares$UrbanPop)
var(linhas_pares$UrbanPop)
sd(linhas_pares$UrbanPop)
