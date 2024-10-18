#Crear un diccionario vacío y lo vaya llenado con información sobre una persona 
#(por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. 
#Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
print(" ")
print("Alvarez Delgado Yael Ismael 3-W 1172")
print(" ")

# Le pedimos los sus datos al usuario
n = str(input('Cual es su nombre? '))
print(" ")
s = str(input('Cual es su sexo? '))
print(" ")
c = str(input('Cual es su correo? '))
print(" ")
t = str(input('Cual es su telefono? '))

# Creamos el diccionario vacio y le agregamos datos
datos = {}
datos['Nombre'] = n 
datos['Sexo'] = s 
datos['Correo'] = c 
datos['Telefono'] = t 

# Mostramos en pantalla toda la informacion guardada en el diccionario vacio
print('Esta es la informacion completa de la persona:', datos)