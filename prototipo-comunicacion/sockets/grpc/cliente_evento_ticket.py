import grpc
import ticket_evento_pb2
import ticket_evento_pb2_grpc


def registrar_evento(stub, tipo_evento, asunto, cliente_id, lamport_timestamp=0):
    response = stub.RegistrarEvento(
        ticket_evento_pb2.EventoTicketRequest(
            ticket_id="",
            tipo_evento=tipo_evento,
            cliente_id=cliente_id,
            asunto=asunto,
            lamport_timestamp=lamport_timestamp,
        )
    )
    print(
        f"[GRPC-CLIENTE] Evento registrado: {response.tipo_evento} | "
        f"Ticket: {response.ticket_id} | Estado: {response.estado} | "
        f"Lamport: {response.lamport_timestamp}"
    )
    return response


def consultar_ticket(stub, ticket_id):
    response = stub.ConsultarTicket(
        ticket_evento_pb2.ConsultarTicketRequest(ticket_id=ticket_id)
    )
    print(
        f"[GRPC-CLIENTE] Consulta: {response.ticket_id} | "
        f"Estado: {response.estado} | Lamport: {response.lamport_timestamp}"
    )
    return response


def main():
    channel = grpc.insecure_channel("localhost:50051")
    stub = ticket_evento_pb2_grpc.EventoTicketServiceStub(channel)

    print("[GRPC-CLIENTE] Registrando evento ticket_creado...")
    resp = registrar_evento(
        stub,
        tipo_evento="ticket_creado",
        asunto="路由器 no responde",
        cliente_id="CLI-001",
        lamport_timestamp=0,
    )

    print("[GRPC-CLIENTE] Consultando ticket...")
    consultar_ticket(stub, resp.ticket_id)


if __name__ == "__main__":
    main()
