palestra1 = {
    "Marley Beltran",
    "Allen Black",
    "Flynn Adams",
    "Ajay Copeland",
    "Keziah Shaw",
    "Junaid Hogan",
    "Leanne Fields",
}

palestra2 = {
    "Tara Blackwell",
    "Jared Salas",
    "Samira Sykes",
    "Junaid Hogan",
    "Leanne Fields",
}

palestra3 = {
    "Flynn Adams",
    "Ajay Copeland",
    "Keziah Shaw",
    "Leanne Fields",
    "Junaid Hogan",
}

participantesAssiduos = list(set.intersection(palestra1, palestra2, palestra3))
participacaoGeral = list(set.union(palestra1, palestra2, palestra3))

participantesAssiduos.sort()
participacaoGeral.sort()

print("Pessoas que participaram de todas as palestras:")
for p in participantesAssiduos:
    print(p)
print("")

print("Presenca geral:")
for p in participacaoGeral:
    print(p)
