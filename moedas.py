import requests
import json
cotacoes= requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes=cotacoes.json()

btc=(float(cotacoes["BTCBRL"]["bid"]))
euro=(float(cotacoes["EURBRL"]["bid"]))
dolar=(float(cotacoes["USDBRL"]["bid"]))
print("------------- COTAÇÕES EM TEMPO REAL-------------")
print("No momento o Dólar está custando, R$:",dolar)
print("No momente o Euro está custando, R$:",euro)
print("No momento o Bitcoin está custando, R$:",btc)
print("-------------------------------------------------")
x=0
print("Para fazer conversões de moedas para R$ digite ( X )")
x=input("Opção:")
if x==x or X:
    print("Para fazer conversões com Dólar, Digite:( 1 )")
    print(("Para fazer conversões com Euro, Digte:  ( 2 )"))

    print("-------------------------------------------------")
    conversao= int(input("Escolhar sua Opção:"))
    if conversao==1:
        print("Conversor Reais para Dólar")
        reais=float(input("Digite o valor em Reais:"))
        reais_pdol=round(reais * dolar,3)
        print("R$:",reais,"equivalem a:", reais_pdol,"Dólares")
    elif conversao==2:
        print("Conversor Reais para Euro")
        euro1=float(input("Digite o Valor em Reais:"))
        reais_peu=round(euro1 * euro,3)
        print("R$:",euro1,"equivalem a:",reais_peu, "Euros")











