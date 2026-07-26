# PFC — Soporte Tecnico ISP

Sistema distribuido de gestion de soporte tecnico para proveedores de servicios de Internet (ISP).

## Entregas

| Entrega | Descripcion | Estado |
|---------|-------------|--------|
| **E1** | Problema fundamentado, arquitectura propuesta, prototipo de comunicacion (sockets, gRPC, Lamport) | En progreso |
| E2 | Microservicios, Docker Compose, Kafka, API Gateway | Pendiente |
| E3 | CockroachDB, Spark, ADRs de fragmentacion | Pendiente |

## Estructura del repositorio

```
proyecto-pfc/
├── README.md
├── pom.xml                          # proyecto Java (microservicios, E2+)
├── docs/
│   ├── problema-soporte-tecnico-isp.md
│   ├── dominio-y-actores-soporte-tecnico.md
│   ├── requisitos-no-funcionales.md
│   ├── estilo-arquitectonico-distribuido.md
│   └── diagrams/
│       └── c4-nivel1-contexto-soporte-tecnico.svg
├── prototipo-comunicacion/          # prototipo tecnico E1
│   ├── README.md
│   ├── sockets/
│   ├── grpc/
│   └── lamport/
├── entrega1/
│   └── PFC_Entrega1.pdf
└── src/                             # codigo Java del sistema (E2+)
```

## Prototipo de comunicacion (E1)

El directorio `prototipo-comunicacion/` contiene tres componentes:

- **sockets/** — Comunicacion cliente-servidor mediante TCP sockets (notificacion de tickets).
- **grpc/** — Servicio gRPC con definicion de contrato `ticket_evento.proto` (eventos del ciclo de vida del ticket).
- **lamport/** — Reloj logico de Lamport para ordenar eventos causalmente entre los dos mecanismos de comunicacion.

Ver [prototipo-comunicacion/README.md](prototipo-comunicacion/README.md) para instrucciones de ejecucion.

## Tecnologias

- **E1:** Python (prototipo de comunicacion)
- **E2+:** Java 21, Maven, Spring Boot, Docker, Kafka, API Gateway
