n1 = int(input("Nivel 1: "))
n2 = int(input("Nivel 2: "))
n3 = int(input("Nivel 3: "))

total = n1 + n2 + n3
print("Puntaje total:", total)

h = int(input("Horas: "))
m = int(input("Minutos: "))
s = int(input("Segundos: "))

total = h*3600 + m*60 + s
print("Total en segundos:", total)

a1 = int(input("Ataque 1: "))
a2 = int(input("Ataque 2: "))
a3 = int(input("Ataque 3: "))

print("Daño total:", a1 + a2 + a3)

max_vida = int(input("Vida máxima: "))
actual = int(input("Vida actual: "))

porcentaje = (actual / max_vida) * 100
print("Vida restante:", porcentaje, "%")

try:
    oro1 = int(input("Ingrese oro del jugador 1: "))
    oro2 = int(input("Ingrese oro del jugador 2: "))
    oro3 = int(input("Ingrese oro del jugador 3: "))

    print("Oro total:", oro1 + oro2 + oro3)
except ValueError:
    print("Error: Debes ingresar solo números enteros.")


d = float(input("Distancia: "))
t = float(input("Tiempo: "))

print("Velocidad:", d / t)

num1 = float(input("Ingrese valor 1: "))
num2 = float(input("Ingrese valor 2: "))
num3 = float(input("Ingrese valor 3: "))

print("Total:", num1 + num2 + num3)


total = int(input("Tiempo total: "))
trans = int(input("Transcurrido: "))

print("Restante:", total - trans)

n1 = int(input("Ingrese número 1: "))
n2 = int(input("Ingrese número 2: "))
n3 = int(input("Ingrese número 3: "))

print("Total:", n1 + n2 + n3)


print("Promedio:", (n1+n2+n3)/3)

base = float(input("Daño base: "))
multi = float(input("Multiplicador: "))

print("Crítico:", base * multi)

minutos = int(input("Ingrese los minutos: "))


h = minutos // 60
m = minutos % 60

print(h, "horas y", m, "minutos")

oro1 = int(input("Oro jugador 1: "))
oro2 = int(input("Oro jugador 2: "))
oro3 = int(input("Oro jugador 3: "))

minutos = int(input("Minutos jugados: "))

total = oro1 + oro2 + oro3

print("Total:", total)

n1 = int(input("Ingrese número 1: "))
n2 = int(input("Ingrese número 2: "))
n3 = int(input("Ingrese número 3: "))
completadas = int(input("Ingrese tareas completadas: "))


print((completadas/total)*100, "%")

def leer_float(mensaje):
    while True:
        dato = input(mensaje)
        if dato.strip() == "":
            print("⚠️ No puedes dejar el campo vacío.")
        else:
            try:
                return float(dato)
            except ValueError:
                print("⚠️ Ingresa un número válido.")

n1 = leer_float("Ingrese valor 1: ")
n2 = leer_float("Ingrese valor 2: ")
n3 = leer_float("Ingrese valor 3: ")

print("Total:", n1 + n2 + n3)


print((int(input())+int(input())+int(input()))/3)

def leer_entero(mensaje):
    while True:
        dato = input(mensaje)
        if dato.strip() == "":
            print("⚠️ No puedes dejar el campo vacío.")
        else:
            try:
                return int(dato)
            except ValueError:
                print("⚠️ Debes ingresar un número válido.")

n1 = leer_entero("Ingrese número 1: ")


derrotados = int(input())

print((derrotados/total)*100, "%")

