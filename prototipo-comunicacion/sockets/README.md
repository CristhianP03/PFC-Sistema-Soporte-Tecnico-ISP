# Prototipo de comunicacion entre procesos

Este directorio contiene el prototipo tecnico de la entrega E1, que demuestra la comunicacion entre procesos utilizando dos mecanismos y un modelo de ordenamiento de eventos, aplicado al dominio de soporte tecnico ISP.

## Componentes

### 1. Sockets TCP (`sockets/`)

Comunicacion directa cliente-servidor mediante TCP sockets para notificacion de eventos de tickets.

**Archivos:**
- `servidor_notificacion_ticket.py` — Escucha conexiones TCP y procesa notificaciones de tickets.
- `cliente_notificacion_ticket.py` — Envia notificacion de ticket_creado al servidor.

**Ejecucion:**
```bash
# Terminal 1
python sockets/servidor_notificacion_ticket.py

# Terminal 2
python sockets/cliente_notificacion_ticket.py
```

### 2. gRPC (`grpc/`)

Comunicacion basada en Protocol Buffers con contrato definido en `ticket_evento.proto` para el ciclo de vida de tickets.

**Archivos:**
- `ticket_evento.proto` — Definicion del servicio y mensajes (ticket_creado, ticket_asignado, ticket_resuelto).
- `servidor_evento_ticket.py` — Implementacion del servicio gRPC.
- `cliente_evento_ticket.py` — Cliente que registra y consulta eventos de tickets.

**Prerrequisitos:**
```bash
pip install grpcio grpcio-tools
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ticket_evento.proto
```

**Ejecucion:**
```bash
# Terminal 1
python grpc/servidor_evento_ticket.py

# Terminal 2
python grpc/cliente_evento_ticket.py
```

### 3. Reloj logico de Lamport (`lamport/`)

Implementacion del algoritmo de Lamport para asignar timestamps logicos a los eventos del ciclo de vida del ticket (creado -> asignado -> resuelto) en procesos distribuidos.

**Archivos:**
- `reloj_lamport.py` — Implementacion del reloj logico con integracion a sockets.

**Ejecucion:**
```bash
python lamport/reloj_lamport.py
```

## Flujo del prototipo

1. El servidor TCP recibe una notificacion de `ticket_creado` y la marca con un timestamp de Lamport.
2. El cliente gRPC envia un evento de creacion de ticket, tambien marcado con Lamport.
3. El reloj de Lamport garantiza el orden causal entre ambos mecanismos de comunicacion.
