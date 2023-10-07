# DupliTP

**DupliTP** es un programa de Python diseñado para encontrar y organizar archivos duplicados en un directorio específico. 
Esta aplicación ayuda a liberar espacio en disco eliminando copias innecesarias de archivos y organizando los duplicados 
en una carpeta separada llamada "duplicados" (Los separa, será tarea tuya eliminar esa carpeta).

## Características

- Busca archivos duplicados en un directorio y sus subdirectorios.
- Organiza los archivos duplicados en una carpeta llamada "duplicados".
- Utiliza la biblioteca "art" para mostrar un título estilizado.
- Proporciona manejo de errores para diferentes situaciones.

## Uso

1. Ejecute el programa utilizando Python.

```python
python duplitp.py
```

2. Se le pedirá que ingrese la ruta del directorio que desea analizar. Ingrese la ruta y presione Enter.

3. El programa buscará archivos duplicados en el directorio especificado y los mostrará en la consola.

4. Los archivos duplicados serán movidos a una carpeta llamada "duplicados" dentro del directorio analizado.

5. Una vez completado el proceso, se mostrará un mensaje de confirmación.

6. Presione Enter para salir del programa.

## Requisitos

- Python 3.x
- La biblioteca "art" (puede instalarse con `pip install art`)

## Limitaciones

- No es capaz de detectar duplicados con nombres diferentes.
- No maneja la comparación de archivos binarios, por lo que dos archivos con el mismo nombre pero diferentes contenidos
  no se considerarán duplicados.

## Créditos

Este programa utiliza la biblioteca "art" para crear texto estilizado en la consola y se basa en funciones ubicadas en el 
módulo "funciones" para encontrar y organizar archivos duplicados.

## Notas

- Asegúrese de que la ruta del directorio ingresada sea válida y tenga permisos de lectura.
- Los archivos duplicados se mueven a la carpeta "duplicados" dentro del directorio especificado, por lo que asegúrese de
  tener suficiente espacio en disco antes de ejecutar el programa.

¡Disfrute de DupliTP y libere espacio en disco eliminando duplicados de manera eficiente!




