#Un conjunto es una colección desordenada de elementos únicos. No permite duplicados y no mantiene el orden de los elementos
Amigos = {"Omar", "Teresa", "Michael"}

print(Amigos)

# Agregar un elemento
Amigos.add("Pedro")
print(Amigos)

# Eliminar un elemento
Amigos.remove("Teresa")
print(Amigos)

# Verificar si un elemento está en el conjunto
print("Michael" in  Amigos)  # Esto imprimirá True
print("Teresa" in Amigos)  # Esto imprimirá False


