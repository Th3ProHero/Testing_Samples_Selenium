import subprocess
import sys

def instalar_biblioteca(nombre_biblioteca):
    try:
        # Utiliza el comando pip para instalar o actualizar la biblioteca
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", nombre_biblioteca])
        print(f"La biblioteca '{nombre_biblioteca}' se ha instalado o actualizado con éxito.")
    except subprocess.CalledProcessError:
        print(f"No se pudo instalar o actualizar la biblioteca '{nombre_biblioteca}'. Verifica que tienes pip instalado y que estás conectado a Internet.")

# Lista de bibliotecas que necesitas para tu código
bibliotecas_requeridas = [
    "pillow",
    "matplotlib",
    "unittest",
    "openpyxl",
    "gspread",
    "virtualenv",
    "selenium",
    "os",
    # Agrega aquí el nombre de las bibliotecas que necesitas
]

if __name__ == "__main__":
    for biblioteca in bibliotecas_requeridas:
        instalar_biblioteca(biblioteca)
