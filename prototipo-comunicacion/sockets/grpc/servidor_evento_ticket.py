import grpc
from concurrent import futures
import ticket_evento_pb2
import ticket_evento_pb2_grpc
import uuid


class EventoTicketServicer(ticket_evento_pb2_grpc.EventoTicketServiceServicer):
    def __init__(self):
        self.tickets = {}

    def RegistrarEvento(self, request, context):
        ticket_id = request.ticket_id or str(uuid.uuid4())[:8]
        lamport = request.lamport_timestamp + 1
        self.tickets[ticket_id] = {
            "tipo_evento": request.tipo_evento,
            "cliente_id": request.cliente_id,
            "asunto": request.asunto,
            "estado": "registrado",
            "lamport": lamport,
        }
        print(
            f"[GRPC-SERVIDOR] Evento '{request.tipo_evento}' registrado | "
            f"Ticket: {ticket_id} | Cliente: {request.cliente_id} | Lamport: {lamport}"
        )
        return ticket_evento_pb2.EventoTicketResponse(
            ticket_id=ticket_id,
            tipo_evento=request.tipo_evento,
            estado="registrado",
            lamport_timestamp=lamport,
            mensaje=f"Evento '{request.tipo_evento}' registrado exitosamente",
        )

    def ConsultarTicket(self, request, context):
        ticket = self.tickets.get(request.ticket_id)
        if ticket:
            return ticket_evento_pb2.EventoTicketResponse(
                ticket_id=request.ticket_id,
                tipo_evento=ticket["tipo_evento"],
                estado=ticket["estado"],
                lamport_timestamp=ticket["lamport"],
                mensaje="Ticket encontrado",
            )
        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details("Ticket no encontrado")
        return ticket_evento_pb2.EventoTicketResponse()


def servir():
    servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ticket_evento_pb2_grpc.add_EventoTicketServiceServicer_to_server(
        EventoTicketServicer(), servidor
    )
    servidor.add_insecure_port("[::]:50051")
    servidor.start()
    print("[GRPC-SERVIDOR] Servidor gRPC escuchando en puerto 50051")
    servidor.wait_for_termination()


if __name__ == "__main__":
    servir()
