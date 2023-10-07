import os
from art import *
from modulos.funciones import (
    encontrar_archivos_duplicados,
    imprimir_duplicados,
    mover_a_duplicados,
)

while True:
    try:
        tprint("DupliTP")
        print("Ingrese la ruta del directorio que desea analizar: ")
        directory_path = input("> ")
        os.system('cls')
        tprint("DupliTP")
        print("Cargando...")

        if not isinstance(directory_path, str):
            print("Error: La ruta ingresada no es una cadena válida.")
            continue

        if not os.path.isdir(directory_path):
            print("Error: La ruta no es un directorio válido.")
            continue

        duplicate_folder = os.path.join(directory_path, "duplicados")
        if not os.path.exists(duplicate_folder):
            os.makedirs(duplicate_folder)

        duplicates = encontrar_archivos_duplicados(directory_path)
        imprimir_duplicados(duplicates)

        for file_hash, file_list in duplicates.items():
            if len(file_list) > 1:
                for file_path in file_list[1:]:
                    mover_a_duplicados(file_path, duplicate_folder)

        print(
            "Proceso completado.\nLos duplicados han sido movidos a la carpeta 'duplicados'."
        )
        input("Presiona Enter para salir...")
        break

    except FileNotFoundError as e:
        print(f"Error: No se encontró el archivo o directorio: {e.filename}")
    except PermissionError as e:
        print(f"Error: Permiso denegado para acceder a {e.filename}")
    except Exception as e:
        print(f"Error desconocido: {str(e)}")

        duplicates = encontrar_archivos_duplicados(directory_path)
        imprimir_duplicados(duplicates)