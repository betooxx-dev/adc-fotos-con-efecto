# Efectos de Cámara en Tiempo Real con OpenCV

Este proyecto es un ejercicio en Python que utiliza la biblioteca OpenCV para aplicar diferentes efectos a la transmisión en vivo de la cámara.

## Descripción

El programa captura video en tiempo real desde la cámara del dispositivo y permite al usuario aplicar diferentes efectos:

1. Color (sin efecto)
2. Escala de grises
3. Efecto de caricatura

Después de aplicar el efecto, el programa guarda la imagen resultante como un archivo JPG.

## Requisitos

- Python 3.x
- OpenCV (cv2)

## Instalación

1. Asegúrate de tener Python 3.x instalado en tu sistema.
2. Instala OpenCV ejecutando:
   ```
   pip install opencv-python
   ```
3. Descarga el archivo `main.py` de este repositorio.

## Uso

1. Ejecuta el script desde la línea de comandos:
   ```
   python main.py
   ```
2. Sigue las instrucciones en pantalla para seleccionar el efecto deseado.
3. La imagen con el efecto aplicado se mostrará en una ventana y se guardará automáticamente.
4. Presiona 'q' en cualquier momento para salir del programa.

## Opciones de Efectos

1. **Color**: Muestra y guarda la imagen original sin efectos.
2. **Escala de grises**: Convierte la imagen a escala de grises.
3. **Caricatura**: Aplica un efecto de caricatura a la imagen.
4. **Salir**: Cierra el programa.

## Estructura del código

- `main()`: Función principal que maneja la captura de video, la selección de efectos y el guardado de imágenes.
- El código utiliza un bucle `while` para capturar continuamente frames de la cámara y aplicar los efectos seleccionados.

## Notas

- Asegúrate de tener una cámara conectada y funcionando en tu dispositivo.
- Las imágenes se guardan en el mismo directorio donde se ejecuta el script.
