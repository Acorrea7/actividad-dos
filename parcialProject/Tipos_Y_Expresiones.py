#Conversion de tipos de datos (enteros, decimales y cadenas)

#Enteros

#This is a comment
print("Hello, World!")

#Enteros
entero_positivo = 42
saldo_bancario = 150000
gran_entero = 9876543210
print(type(saldo_bancario))

#Decimales
precio_por_kilo = 2.99
decimal_negativo = -1.5
decimal_preciso = 2.71828
print(type(precio_por_kilo))

#Cadenas
nombre_completo = "Zhamuel Rosero"
telefono = "+34 612 345 678"
codigo_postal = "28001"
pagina_web = "www.ejemplo.com"
print(type(nombre_completo))

#Multiliena de cadenas

direccion = """Calle Falsa 123,
Piso 4, 
Apto B,
Madrid, España."""
print(type(direccion))

#Funcion lean().

nombre = "Cristiano Ronaldo"
longitud_nombre = len(nombre)
print(type(longitud_nombre))

#Sub cadenas **** Obtener los primeros n caracteres de una cadena:

# Ejemplo de cadena
texto = "Cristiano Ronaldo Es Un Gran Futbolista."

#Obtener los primeros n caracteres de una cadena.
n = 10
primero_n = texto[:n]
print("Primeros",n, "Caracteres",primero_n)
#Obtener los caracteres de en medio de una cadena.
medio = direccion[40:80]
print("Caracteres de en medio (índices 40 a 80):", medio)

# Obtener los últimos n caracteres
ultimos_n = direccion[-10:]
print("Últimos", n, "caracteres:", ultimos_n)

#Upper()
mayus = texto.upper()
print(mayus)

#Lower()
minusculas = texto.lower()
print(minusculas)

#Multilíneas de cadenas de caracteres.
discurso = """Me voy pero esta camiseta, este escudo y el Santiago Bernabéu los seguiré sintiendo siempre como algo mío esté donde esté.
Gracias a todos y, por supuesto, como dije aquella primera vez en nuestro estadio hace 9 años: ¡Hala Madrid!"""


print("Cadena multilínea de caracteres:")
print(discurso)


#Función strip()

discurso_limpio = discurso.strip()
print(discurso_limpio)

#Función replace()
# Usando replace() para reemplazar "camiseta" por "uniforme"
discurso_modificado = discurso.replace("camiseta", "uniforme")

print(discurso_modificado)

#Funcion Split
# Usando split() para dividir el discurso en palabras
palabras = discurso.split()

print(palabras)

#Formato de cadenas F-String

nombre_jugador = "Cristiano Ronaldo"
anio = 9
camiseta = "Real Madrid"

discurso = f"""Me voy pero esta camiseta {camiseta} , este escudo y el Santiago Bernabéu los seguiré sintiendo siempre como algo mío esté donde esté.
Gracias a todos y, por supuesto, como dije aquella primera vez en nuestro estadio hace {anio} años: ¡Hala Madrid!"""

print(discurso)
