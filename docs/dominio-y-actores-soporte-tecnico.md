# Dominio y Actores — Soporte Tecnico ISP

## 1. Dominio

El sistema abarca la **gestion del ciclo de vida de solicitudes de soporte de conectividad a Internet**:

```
Recepcion -> Clasificacion -> Asignacion -> Atencion -> Resolucion -> Cierre
```

Cada solicitud (ticket) representa una incidencia reportada por un cliente que requiere intervencion tecnica o administrativa.

> **Fuente:** E2, cap. 2.1 (glosario de terminos del dominio).

## 2. Actores

| Actor | Rol | Interacciones principales |
|-------|-----|--------------------------|
| **Cliente** | Usuario del servicio de Internet que reporta una incidencia. | Crea solicitudes, consulta estado, recibe notificaciones de resolucion. |
| **Tecnico** | Profesional asignado para resolver la incidencia. | Recibe asignaciones, actualiza estado, registra acciones realizadas. |
| **Personal administrativo** | Supervisa y coordina el flujo de soporte. | Visualiza metricas, gestiona asignaciones, genera reportes. |

> **Fuente:** E2, cap. 1.1.2 y cap. 2.1 (actores identificados en el dominio de soporte tecnico).

## 3. Ciclo de vida de una solicitud

```
┌─────────┐     ┌──────────────┐     ┌────────────┐     ┌───────────┐     ┌──────────┐
│ Cliente  │---->│  Solicitud   │---->│ Asignacion │---->│ Atencion  │---->│ Resuelto │
│ crea     │     │  registrada  │     │ a tecnico  │     │ en curso  │     │          │
└─────────┘     └──────────────┘     └────────────┘     └───────────┘     └──────────┘
                                                                  │
                                                                  v
                                                           ┌───────────┐
                                                           │  Cerrado  │
                                                           └───────────┘
```

## 4. Fuentes

- **E3:** "quedaron establecidos el dominio, los actores" — requisito explícito de la entrega E1.
- **E2, cap. 1.1.2:** actores identificados (Cliente, Tecnico, Personal administrativo).
- **E2, cap. 2.1.1:** glosario del dominio (Ticket, Cliente, Tecnico, Solicitud).
