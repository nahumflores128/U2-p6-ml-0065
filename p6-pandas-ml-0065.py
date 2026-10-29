import pandas as pd
import numpy as np

serie_amigos=["Michelle", "Hugo", "Iker", "Nahum", "Ricardo", "Anais"]
print(" ---  Serie listado de amigos NC 0065")
amigos=pd.Series(serie_amigos)
print(amigos)

serie_billetes=[20,50,100,200,500,1000]
print(" ---  Serie listado de billetes NC 0065")
billetes=pd.Series(serie_billetes)
print(billetes)

serie_billetes=[20,50,100,200,500,1000]
serie_bletras=["viente","cimcuenta","cien","docientos", "quinientos","mil"]
print(" ---  Serie listado de nombres y valor de billetes NC 0065")
tablabilletes=pd.Series(serie_billetes, index=serie_bletras)
print(tablabilletes)

# diccionario dataframe
# monedas de valor y nombre
print("datos de diccionario a Dataframe en pandas")
dic_monedas={ 
 "serie_billetes": [20, 50, 100, 200, 500, 1000],  # <--- Coma agregada
 "serie_bletras": ["veinte", "cimcuenta", "cien", "docientos", "quinientos", "mil"]
}

tablabilletes=pd.DataFrame(dic_monedas,index=["A","B","C","D","E","F"])
print(tablabilletes)
print("Casa de cambio de Nahum flored NC 0065")