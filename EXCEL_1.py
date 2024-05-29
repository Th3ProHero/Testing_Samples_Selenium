import openpyxl

# Nombre del archivo Excel en la misma ubicación que el script
archivo_excel = 'ELEMENTS.xlsx'

# Cargar el archivo Excel
libro = openpyxl.load_workbook(archivo_excel)
hoja = libro.active

# Variables para almacenar los valores
CorreoValue = []
Contraseña = []

# Recorrer las filas de la hoja, empezando desde la segunda fila (ignorando la primera)
for fila in hoja.iter_rows(min_row=2, values_only=True):
    correo = str(fila[1])  # Columna B
    contraseña = str(fila[2])  # Columna C
    CorreoValue.append(correo)
    Contraseña.append(contraseña)

# Imprimir los valores en la consola
for correo, contraseña in zip(CorreoValue, Contraseña):
    print("Correo:", correo)
    print("Contraseña:", contraseña)
    print()

# Cerrar el archivo
libro.close()