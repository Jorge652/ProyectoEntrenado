from ultralytics import YOLO
import cv2

# Leer nuestro modelo
model = YOLO('best.pt')

# Realizar VideoCaptura
cap = cv2.VideoCapture(0)

# Bucle

while True:
    # Leer nuestros fotogramas
    ret, frame = cap.read()

    # Leemos resultados
    resultados = model.predict(frame, imgsz=640, conf=0.90)

    anotaciones = resultados[0].plot()

    cv2.imshow("DETECCION Y SEGMENTACION", anotaciones)

    # Cerrar el programa
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()