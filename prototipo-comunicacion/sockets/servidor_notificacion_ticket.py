import socket
import json
import threading

HOST = "127.0.0.1"
PORT = 65432


def manejar_cliente(conn, addr):
    print(f"[SERVIDOR] Conexion desde {addr}")
    with conn:
        while True:
            data = conn.recv(4096)
            if not data:
                break
            evento = json.loads(data.decode("utf-8"))
            print(f"[SERVIDOR] Evento recibido: {evento}")

            respuesta = {
                "status": "ok",
                "mensaje": f"Ticket '{evento.get('asunto', '')}' registrado",
                "ticket_id": evento.get("ticket_id", "N/A"),
                "lamport": evento.get("lamport", 0) + 1,
            }
            conn.sendall(json.dumps(respuesta).encode("utf-8"))
            print(f"[SERVIDOR] Respuesta enviada: {respuesta}")


def iniciar_servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        print(f"[SERVIDOR] Escuchando en {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            threading.Thread(target=manejar_cliente, args=(conn, addr), daemon=True).start()


if __name__ == "__main__":
    iniciar_servidor()
