import socket
import json
import uuid

HOST = "127.0.0.1"
PORT = 65432


def notificar_ticket_creado(asunto, cliente_id, lamport_tick=0):
    evento = {
        "ticket_id": str(uuid.uuid4())[:8],
        "tipo_evento": "ticket_creado",
        "asunto": asunto,
        "cliente_id": cliente_id,
        "lamport": lamport_tick,
    }
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(json.dumps(evento).encode("utf-8"))
        data = s.recv(4096)
        respuesta = json.loads(data.decode("utf-8"))
        print(f"[CLIENTE] Respuesta: {respuesta}")
        return respuesta


if __name__ == "__main__":
    print("[CLIENTE] Notificando ticket_creado por socket TCP...")
    notificar_ticket_creado("No hay conexion a Internet", cliente_id="CLI-001")
