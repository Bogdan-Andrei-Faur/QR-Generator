# QR Code Generator

Este repositorio contiene un script de Python que genera códigos QR a partir de URLs proporcionadas por el usuario. El script utiliza `tkinter` para la interfaz gráfica y `qrcode` para la generación del código QR. También se proporciona una guía para crear un ejecutable autónomo utilizando PyInstaller.

## Requisitos

- Python 3.x
- Paquetes de Python: `qrcode`, `Pillow` (para soporte de imágenes en `qrcode`), `tkinter` (viene incluido con Python en Mac)

Puedes instalar los paquetes necesarios con el siguiente comando:

    pip install qrcode[pil]

## Uso del Script

El script generador.py proporciona una interfaz gráfica donde el usuario puede ingresar una URL y generar un código QR que puede ser guardado como un archivo PNG.
Ejecución del Script

Para ejecutar el script, asegúrate de estar en el directorio donde se encuentra generador.py y usa el siguiente comando:

    python generador.py

## Funcionalidades:

    Ingresar URL: Ingresa la URL en el campo de entrada.
    
    Generar QR: Haz clic en el botón "Generar QR" para crear el código QR.
    
    Guardar el código QR: Se abrirá un cuadro de diálogo para guardar el código QR como un archivo PNG.

## Crear un Ejecutable con PyInstaller

Para compartir el programa con personas que no tienen conocimientos de programación, puedes crear un ejecutable autónomo utilizando PyInstaller.
Instalación de PyInstaller

Si no tienes PyInstaller instalado, puedes instalarlo usando pip:

    pip install pyinstaller

## Generar el Ejecutable

Navega al directorio donde se encuentra generador.py y el archivo de icono cropped-favicon.ico. Luego, ejecuta el siguiente comando:

    pyinstaller --onefile --windowed --icon=logo.ico generador.py

Este comando creará un único archivo ejecutable en el directorio dist. Puedes compartir este archivo ejecutable con tus compañeros de trabajo.
Estructura del Proyecto

    QR-Generator/
    │
    ├── generador.py         # Script principal para generar códigos QR
    ├── logo.ico  # Icono de la aplicación
    └── README.md            # Este archivo

## Contribuir

Si deseas contribuir a este proyecto, por favor realiza un fork del repositorio, crea una nueva rama con tus cambios y envía un pull request o contacta conmigo por email bogdan.andrei.faur@gmail.com.
Licencia

Este proyecto está bajo la MIT License.

Este archivo `README.md` incluye todas las instrucciones necesarias para ejecutar el script, instalar dependencias y generar un ejecutable con PyInstaller. Simplemente coloca este contenido en un archivo llamado `README.md` en tu repositorio.

