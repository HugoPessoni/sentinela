import cv2
import time

def test_camera():
    # Tenta abrir a webcam (por padrão, índice 0)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Não foi possível acessar a câmera.")
        return

    # Defina a resolução desejada (ex: 640x480). Ajuste conforme necessário.
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # Para medir FPS
    frame_count = 0
    start_time = time.time()

    print("Pressione 'q' na janela para encerrar.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Erro na captura do frame.")
            break

        frame_count += 1

        # (Opcional) Se quiser exibir a imagem em uma janela
        cv2.imshow('Teste da Cam', frame)

        # Verifica se a tecla 'q' foi pressionada
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    end_time = time.time()
    elapsed = end_time - start_time
    cap.release()
    cv2.destroyAllWindows()

    # Calcula e printa o FPS aproximado
    if elapsed > 0:
        fps = frame_count / elapsed
        print(f"FPS médio: {fps:.2f}")

if __name__ == "__main__":
    test_camera()
