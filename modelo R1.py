##################
# MODELO DE RECONOCIMIENTO DE INTESIDAD DE LUZ EN UNA IAMGEN
#19-3-26
#################
imagenDigital = [
     [255, 120,  0],
     [200, 255, 150],
     [10, 50, 255]
     

]
print("--Escaneado matriz de imagen--")
print(f"{'Coordenada':<15} | {'valor': <8}| {'Resultado'}")
print("*" *40)


umbral = 128
filaCont = 0
for fila in imagenDigital:
    columnaCont = 0
    for pixel in fila:
        if pixel >= umbral:
            resultado = "Luz"
        else:
            resultado = "SOMBRA"

        print(f"Pixel [{filaCont}],{columnaCont}]| {pixel:<8} | {resultado} ")
        columnaCont +=1
    filaCont += 1


print("*" * 40 )
print("Escaneo completado, nuestra IA ha interpretado la matriz")
