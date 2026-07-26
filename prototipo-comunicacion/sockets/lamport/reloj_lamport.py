import threading
import time


class RelojLamport:
    """Implementacion del reloj logico de Lamport."""

    def __init__(self):
        self._contador = 0
        self._lock = threading.Lock()

    @property
    def valor(self):
        with self._lock:
            return self._contador

    def incrementar(self):
        """Incrementa el reloj local (evento interno o envio)."""
        with self._lock:
            self._contador += 1
            return self._contador

    def actualizar(self, timestamp_recibido):
        """Actualiza el reloj al recibir un mensaje: max(local, recibido) + 1."""
        with self._lock:
            self._contador = max(self._contador, timestamp_recibido) + 1
            return self._contador

    def __repr__(self):
        return f"RelojLamport({self._contador})"


def simular_eventos():
    """Simula eventos del ciclo de vida de un ticket entre procesos distribuidos."""

    reloj_cliente = RelojLamport()
    reloj_tecnico = RelojLamport()

    print("=== Simulacion de reloj logico de Lamport ===")
    print("    Eventos del ciclo de vida de un ticket\n")

    # Proceso Cliente: crea ticket
    ts1 = reloj_cliente.incrementar()
    print(f"[CLIENTE]   ticket_creado          -> Lamport = {ts1}")

    # Proceso Cliente: notifica al tecnico
    ts2 = reloj_cliente.incrementar()
    print(f"[CLIENTE]   envia notificacion     -> Lamport = {ts2}")

    # Simular latencia de red
    time.sleep(0.1)

    # Proceso Tecnico: recibe notificacion
    ts3 = reloj_tecnico.actualizar(ts2)
    print(f"[TECNICO]   recibe notificacion    -> Lamport = {ts3}")

    # Proceso Tecnico: ticket asignado
    ts4 = reloj_tecnico.incrementar()
    print(f"[TECNICO]   ticket_asignado        -> Lamport = {ts4}")

    # Proceso Tecnico: ticket resuelto
    ts5 = reloj_tecnico.incrementar()
    print(f"[TECNICO]   ticket_resuelto        -> Lamport = {ts5}")

    # Proceso Tecnico: notifica resolucion al cliente
    ts6 = reloj_tecnico.incrementar()
    print(f"[TECNICO]   envia respuesta        -> Lamport = {ts6}")

    # Simular latencia de red
    time.sleep(0.1)

    # Proceso Cliente: recibe respuesta
    ts7 = reloj_cliente.actualizar(ts6)
    print(f"[CLIENTE]   recibe respuesta       -> Lamport = {ts7}")

    print(f"\nEstado final: Cliente={reloj_cliente}, Tecnico={reloj_tecnico}")
    print("\n=== Verificacion de orden causal ===")
    print(f"  ticket_creado (ts={ts1}) < ticket_asignado (ts={ts4}): {ts1 < ts4}")
    print(f"  ticket_asignado (ts={ts4}) < ticket_resuelto (ts={ts5}): {ts4 < ts5}")
    print(f"  envio Tecnico (ts={ts6}) < recepcion Cliente (ts={ts7}): {ts6 < ts7}")


def integrar_con_socket():
    """Demostracion de integracion con sockets TCP."""
    import socket
    import json
    import threading

    HOST = "127.0.0.1"
    PORT = 65435

    reloj_servidor = RelojLamport()

    def servidor():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((HOST, PORT))
            s.listen(1)
            conn, _ = s.accept()
            with conn:
                data = conn.recv(4096)
                msg = json.loads(data.decode())
                ts = reloj_servidor.actualizar(msg["lamport"])
                print(f"\n[LAMPORT-SERVIDOR] Evento '{msg.get('tipo_evento', 'N/A')}' | Lamport={msg['lamport']} -> Actualizado={ts}")
                respuesta = {"status": "ok", "lamport": ts}
                conn.sendall(json.dumps(respuesta).encode())

    def cliente():
        reloj_cliente = RelojLamport()
        time.sleep(0.2)
        ts = reloj_cliente.incrementar()
        msg = {"tipo_evento": "ticket_creado", "ticket_id": "TK-001", "lamport": ts}
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(json.dumps(msg).encode())
            data = s.recv(4096)
            resp = json.loads(data.decode())
            print(f"[LAMPORT-CLIENTE] ticket_creado Lamport={ts} -> Respuesta Lamport={resp['lamport']}")

    print("\n=== Integracion Lamport + Socket ===")
    t_serv = threading.Thread(target=servidor, daemon=True)
    t_serv.start()
    cliente()
    t_serv.join(timeout=2)


if __name__ == "__main__":
    simular_eventos()
    integrar_con_socket()
