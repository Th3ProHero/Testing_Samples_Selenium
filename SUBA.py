import numpy as np
import openpyxl

# Inicializar arreglos
mails = []
passwords = []

# Cargar el archivo Excel
archivo_excel = "LOG11.xlsx"  # Reemplaza con el nombre de tu archivo Excel

# Leer datos del archivo Excel
wb = openpyxl.load_workbook(archivo_excel)
sheet = wb.active

for row in sheet.iter_rows(min_row=2, max_col=3):  # Empezar desde la fila 2 y leer columnas B y C
    if row[0].value is None:  # Verificar si la celda en la Columna A está vacía
        break  # Salir del bucle si la celda en la Columna A está vacía

    mails.append(row[1].value)  # Agregar el valor de la celda en la Columna B a "mails"
    passwords.append(row[2].value)  # Agregar el valor de la celda en la Columna C a "passwords"

# Cerrar el archivo Excel
wb.close()

# Mostrar los arreglos resultantes
print("mails:", mails)
print("passwords:", passwords)


def dividir_dos_arreglos_optimo(arr1, arr2, prefix1='mail', prefix2='password'):
    if len(arr1) != len(arr2):
        raise ValueError("Los dos arreglos deben tener la misma longitud.")

    num_elementos = len(arr1)
    num_subarreglos = int(np.sqrt(num_elementos))  # Ajusta esta fórmula según tus necesidades

    subarreglos_nombres = {}
    subarreglos_suma = {}  # Diccionario para almacenar las sumas

    for i in range(num_subarreglos):
        subarreglo1 = arr1[i * num_elementos // num_subarreglos:(i + 1) * num_elementos // num_subarreglos]
        subarreglo2 = arr2[i * num_elementos // num_subarreglos:(i + 1) * num_elementos // num_subarreglos]

        subarreglos_nombres[f"{prefix1}{i + 1}"] = subarreglo1
        subarreglos_nombres[f"{prefix2}{i + 1}"] = subarreglo2

        suma = [x + y for x, y in zip(subarreglo1, subarreglo2)]
        subarreglos_suma[f"RESULT{i + 1}"] = suma

    return subarreglos_nombres, subarreglos_suma

# Ejemplo de uso
arreglo1 = mails  # Primer arreglo 
arreglo2 = passwords  # Segundo arreglo 

subarreglos_nombres, subarreglos_suma = dividir_dos_arreglos_optimo(arreglo1, arreglo2)

# Mostrar subarreglos y sumas
for nombre, subarreglo in subarreglos_nombres.items():
    print(f"{nombre}: {subarreglo}")

# Contar subarreglos de correo (mail) y contraseña (password)
num_subarreglos_correo = sum(1 for nombre in subarreglos_nombres if nombre.startswith('mail'))
num_subarreglos_contrasena = sum(1 for nombre in subarreglos_nombres if nombre.startswith('password'))

# Obtener la cantidad de elementos en cada subarreglo
elementos_por_subarreglo_correo = [len(subarreglo) for nombre, subarreglo in subarreglos_nombres.items() if nombre.startswith('mail')]
elementos_por_subarreglo_contrasena = [len(subarreglo) for nombre, subarreglo in subarreglos_nombres.items() if nombre.startswith('password')]

# Mostrar información
print("Número total de subarreglos de correo:", num_subarreglos_correo)
print("Número total de subarreglos de contraseña:", num_subarreglos_contrasena)

print("\nDetalles de subarreglos de correo:")
for i, elementos in enumerate(elementos_por_subarreglo_correo, start=1):
    print(f"Subarreglo {i}: {elementos} elementos")

print("\nDetalles de subarreglos de contraseña:")
for i, elementos in enumerate(elementos_por_subarreglo_contrasena, start=1):
    print(f"Subarreglo {i}: {elementos} elementos")
    
#  RECORRER LOS ARREGLOS

