# Los diccionarios consumen más espacio porque almacenan pares clave-valor y usan tablas hash para un acceso rápido.
# Su estructura, basada en corchetes, almacena tanto claves como valores, lo cual los hace difenrenciarse de listas o tuplas.
#Si utilizaramos el ejemplo anterior de las listas, podria verse así en diccionarios.
Familia = {
    "Padre": "Jorge",
    "Madre": "Camila",
    "Hija": "Alissa",
    "Hijo": "Erick"
}
print(Familia)

Random = {
    1 : "Peras",
    2 : "Yugioh",
    3 : "Fortnite",
    "Javier" : 3
}
print(Random)