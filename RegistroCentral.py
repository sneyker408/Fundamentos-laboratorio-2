print("................................")
print("Promedio de infracciones")
print("................................")


infracciones = int(input("ingresa la cantidad de infraciones en el mes: "))

infraccionesDiarias = infracciones // 30

matutinas = infraccionesDiarias * 0.20
vespertino = infraccionesDiarias * 0.35
nocturnas = infraccionesDiarias * 0.45


print("el promedio diario matutino de infraciones es de:", matutinas)
print("el promedio diario vespertino de infraciones es de:", vespertino)
print("el promedio diario nocturnas de infraciones es de:", nocturnas)

print("Fin del programa")