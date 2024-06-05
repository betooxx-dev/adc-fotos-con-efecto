import cv2

def main():
    # Inicializar la cámara
    cap = cv2.VideoCapture(0)
    
    while True:
        # Capturar un frame de la cámara
        ret, frame = cap.read()
        
        if not ret:
            print("Error al capturar el frame")
            break
        
        print("Seleccione una opción:")
        print("1. Color")
        print("2. Escala de grises")
        print("3. Caricatura")
        print("4. Salir")
        
        opcion = input("Opción: ")
        
        if opcion == "1":
            # Mostrar la imagen en color
            cv2.imshow('Foto', frame)
        elif opcion == "2":
            # Mostrar la imagen a escala de grises
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('Foto', gray)
        elif opcion == "3":
            # Mostrar la imagen con efecto de caricatura
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (0,0), 5)
            cartoon = cv2.divide(gray, blur, scale=256)
            cv2.imshow('Foto', cartoon)
        elif opcion == "4":
            break

        # Esperar a que se presione una tecla y comprobar si se presionó 'q' para salir
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar la cámara y cerrar las ventanas
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
