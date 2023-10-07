import os
import hashlib
import shutil


def calcular_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while True:
            data = f.read(65536)
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()


def mover_a_duplicados(file_path, duplicate_folder):
    duplicate_path = os.path.join(duplicate_folder, os.path.basename(file_path))
    shutil.move(file_path, duplicate_path)


def encontrar_archivos_duplicados(directory_path):
    duplicates = {}

    for root, dirs, files in os.walk(directory_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_hash = calcular_hash(file_path)

            if file_hash in duplicates:
                duplicates[file_hash].append(file_path)
            else:
                duplicates[file_hash] = [file_path]

    return duplicates


def imprimir_duplicados(duplicates):
    for file_hash, file_list in duplicates.items():
        if len(file_list) > 1:
            print("="*50)
            file_name = os.path.basename(file_list[0])
            print(f"Duplicados de {file_name}:")
            for file_path in file_list[1:]:
                print(f"   {os.path.basename(file_path)}")
            print("="*50)