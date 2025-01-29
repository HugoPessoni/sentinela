import cv2

def test_face_detection():
    # Carrega o Haar Cascade (ajuste o caminho do arquivo, se necessário)
    face_cascade = cv2.CascadeClassifier('/home/orangepi/Desktop/sentinela/haarcascade_frontalface_default.xml')
    if face_cascade.empty():
        print("Não foi possível carregar o arquivo de cascade. Verifique o caminho.")
        return

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Não foi possível acessar a câmera.")
        return

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240)
    print("Pressione 'q' para sair.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Erro na leitura do frame.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Detecta rostos
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        # Desenha retângulo em cada rosto detectado
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow('Deteccao de Rosto - Haar', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    test_face_detection()
