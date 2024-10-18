# Hacer un diccionario de traducción español-inglés, 
# se van a introducir las palabras en español e inglés separadas por dos puntos, 
# y cada par <palabra>:<traducción> separados por comas. El programa debe crear un 
# diccionario con las palabras y sus traducciones. Después pedirá una frase en español 
# y utilizará el diccionario para traducirla palabra a palabra. 
# Si una palabra no está en el diccionario debe dejarla sin traducir.


dic = dict() # Crear un diccionario vacío

# Solicitar al usuario que ingrese palabras en español y sus traducciones
# El formato esperado es: "palabra1:traducción1, palabra2:traducción2"
palabra = str(input('Introducir las palabras y sus traducciones (formato: palabra:traducción, separadas por comas): '))

for i in palabra.split(","): # Recorrer cada par palabra:traducción separado por comas
    
    d = i.split(":") # Dividir cada par por ":" para separar la palabra en español de su traducción
    v = dic.setdefault(d[0], d[1])# Agregar la palabra en español como clave y la traducción como valor en el diccionario


frase = str(input('Escribir una frase en español: ')) # Solicitar al usuario que introduzca una frase en español)
h = frase.split()# Dividir la frase en palabras individuales

print(dic) # Mostrar el diccionario de traducciones 
print(h) # Mostrar la lista de palabras de la frase ingresada

# Recorrer cada palabra en el diccionario de traducciones
for x in dic:
    # Recorrer cada palabra de la frase ingresada
    for z in range(0, len(h)):
        # Si la palabra de la frase coincide con una clave del diccionario
        if x == h[z]:
            # Obtener la traducción de la palabra
            valor = dic.get(h[z])
            # Reemplazar la palabra en español por su traducción
            h[z] = valor
        else:
            continue

# Unir las palabras traducidas en una sola cadena de texto
t = " ".join(h)

# Mostrar la frase traducida
print(t)
