#Médias de prisões por assaltos, estupros e assassinatos das
#5 maiores populações
maior <- c(0,0,0,0,0)
maior[1] <- USArrests$UrbanPop[1]#Valor base para a comparação

#Busca da maior população
tamanho <- 50
for (i in 2:tamanho) {
  if (USArrests$UrbanPop[i] > maior[1]){
    maior[1] <- USArrests$UrbanPop[i]
  }
}

#Tratamento de empates com a maior população
contador <- 1 
for (i in 1:tamanho){
  if ((USArrests$UrbanPop[i] == maior[contador]) & (contador <= 5)){
    maior[contador] <- maior[1]
    if (contador <= 5){
      contador <- contador + 1
    }
  }
}

#Busca pela segunda maior população

#Atribuição de um valor para o segundo elemento do vetor maior 
#(não pode ser um valor igual ao maior valor já armazenado)

#Definição do i-ésimo valor do dataset a ser considerado
#como base para a comparação
if (contador <= 5){
  i <- 1
  flag <- TRUE
  while ((i <= tamanho) & (flag == TRUE)){
    if (USArrests$UrbanPop[i] !=  maior[1]){
      flag <- FALSE
    }else {
      i <- i + 1
    }
  }
}

#Continuação da busca pela segunda maior população
#e busca pela terceira, quarta e quinta maiores
maior_ <- maior[1]
while (contador <= 5){
  #Utilização do i-ésimo valor do dataset
  maior[contador] <- USArrests$UrbanPop[i]
  for (indice in 1:tamanho){
    if ((USArrests$UrbanPop[indice] > maior[contador]) & 
        (USArrests$UrbanPop[indice] < maior_)){
      maior[contador] <- USArrests$UrbanPop[indice]
    }
  }
  
  #Tratamento de empates para a segunda, terceira, quarta e quinta populações
  
  #Uso da variável contador2 para os índices de elementos
  #empatados com o elemento de índice contador
  contador2 <- contador 
  for (indice in 1:tamanho){
    if ((USArrests$UrbanPop[indice] == maior[contador]) & (contador2 <= 5)){
      maior[contador2] <- maior[contador]
      if (contador2 <= 5){
        contador2 <- contador2 + 1
      }
    }
  }
  
  #Atribuição de valores para o terceiro, quarto e quinto elementos do vetor maior 
  #(não pode ser um valor igual ao maior valor já armazenado)
  
  #Definição do i-ésimo valor do dataset a ser considerado
  #como base para a comparação
  if (contador2 <= 5){
    i <- 1 #índice de cada linha do dataset
    flag <- TRUE
    while ((i <= tamanho) & (flag == TRUE)){
      #Verificar todas as populações do dataset
      #com todos os elementos armazenados no vetor
      j <- 1 #índice de cada elemento do vetor
      while (j <= contador2){ 
        if (USArrests$UrbanPop[i] == maior[j]){
          i <- i + 1
          j <- contador2 
        } else if (j == contador2) { 
          flag <- FALSE
        }
        j <- j + 1
      }
    }
  }
  
  #Atualização do maior elemento, decrementando (a segunda
  #maior população, a terceira maior etc, a cada passo da
  #repetição)
  maior_ <- maior[contador]
  contador <- contador2
}

#Atribuição de valor -1 para os elementos que empatam com
#determinado elemento. Não utilizar na soma para não duplicar
contador <- 1
while (contador <= 5) {
  i <- contador + 1
  while (i <= 5){
    if ((maior[contador] == maior[i]) & (maior[i] != -1)){
      maior[i] <- -1
    }
    i <- i + 1
  }
  contador <- contador + 1
}

#Cálculo das somas das prisões, comparando cada elemento do
#vetor com as populações de cada linha do dataset,
#excluindo os elementos iguais a -1
#Se tiver um empate entre o 5ª e a 6ª população, será
#considerada a primeira que é acessada no dataset
#na execução da estrutura de repetição, da observação 1
#para a observação 50
contador <- 1
somaMurder <- 0
somaAssault <- 0
somaRape <- 0
contador2 <- contador
while (contador <= 5){
  for (i in 1:tamanho){
    if ((maior[contador] == USArrests$UrbanPop[i]) & (contador2 <= 5)){
      somaMurder <- somaMurder + USArrests$Murder[i]
      somaAssault <- somaAssault + USArrests$Assault[i]
      somaRape <- somaRape + USArrests$Rape[i]
      contador2 <- contador2 + 1
    }
  }
  contador <- contador2
}

#Cálculo das médias
mediaMurder <- somaMurder/5
mediaAssault <- somaAssault/5
mediaRape <- somaRape/5

#Exibição das médias
mediaMurder
mediaAssault
mediaRape

