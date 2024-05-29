import os
import subprocess

def create_virtualenv(name):
    try:
        # Comprueba si el directorio ya existe
        if os.path.exists(name):
            print(f"El directorio '{name}' ya existe. Elige un nombre diferente.")
            return

        # Crea el directorio para el virtualenv
        os.makedirs(name)

        # Crea el virtualenv en el directorio especificado
        os.system(f"virtualenv {name}")

        print(f"Máquina virtual '{name}' creada exitosamente en '{os.path.abspath(name)}'")
    except Exception as e:
        print(f"Error al crear la máquina virtual: {e}")

if __name__ == "__main__":
    vm_name = input("Ingresa el nombre de la máquina virtual: ").strip()

    if vm_name:
        create_virtualenv(vm_name)

        # Preguntar si se desea ejecutar el instalador
        install_script = input("¿Deseas ejecutar el instalador (installer.py)? (Sí/No): ").strip()
        if install_script.lower() == "si":
            activate_cmd = f"{vm_name}\\Scripts\\activate && python installer.py"
            subprocess.run(activate_cmd, shell=True)
        else:
            print("No se ejecutó el instalador.")
    else:
        print("El nombre de la máquina virtual no puede estar vacío.")
