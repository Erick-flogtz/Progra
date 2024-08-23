# Las tuplas son similares a las listas, pero sus valores no se pueden modificar.
# No necesitan paréntesis para definirse, lo que las define son las comas que separan los elementos.
# Son útiles para almacenar valores específicos y constantes.
# Aunque puedes anidar tuplas, hacerlo puede complicar el código y hacerlo menos "pythónico".
tupla = "Erick","Gabriel",10
print(tupla)

tupla2 = 2000,"Gonzalo","Mole"

tupla_anidada = tupla + tupla2
print(tupla_anidada)

lista_super = ("Cereal","Papitas","Huevo","Pescado")


ultima_tupla = tupla_anidada,lista_super
print(ultima_tupla)
