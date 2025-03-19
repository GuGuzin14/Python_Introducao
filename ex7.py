km = float(input("coloque a distancia em KM: "))
consumo = float(input("coloque o consumo em litros por km: "))

consumoMedio = km / consumo

if(consumoMedio < 8):
    print("Venda o carro!")
elif(consumoMedio >= 8 and consumoMedio <= 12):
    print("Pense em vender o carro!")
elif(consumoMedio > 12):
    print("economico!")