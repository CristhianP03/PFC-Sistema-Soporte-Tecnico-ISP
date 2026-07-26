# Requisitos No Funcionales

Los siguientes requisitos no funcionales se derivan de la justificacion de una arquitectura distribuida para el sistema de soporte tecnico ISP.

## 1. Disponibilidad

Si una parte del sistema falla, las demas continuan funcionando. Un punto unico de fallo no debe dejar fuera todo el servicio de soporte.

> **Fuente:** E2, cap. 1.1.3 — "si una parte falla las demas siguen funcionando" (cita literal).

**Criterio verificable:** Si un proceso se detiene, los demas continuan respondiendo.

## 2. Escalabilidad

El sistema debe permitir el crecimiento del volumen de solicitudes sin degradacion significativa del rendimiento. Cada componente debe poder escalar de forma independiente, refuerzandose solo la parte que lo necesita.

> **Fuente:** E2, cap. 1.1.3 — "se refuerza solo la parte que lo necesita" (cita literal).

**Criterio verificable:** El agregado de instancias de un componente no requiere modificaciones en los demas.

## 3. Mantenibilidad

Cada componente del sistema debe ser modificable sin afectar a los demas. Los cambios en un modulo no deben forzar cambios en otros modulos.

> **Fuente:** E2, cap. 1.1.3 — "se modifica una parte sin afectar el resto" (cita literal).

**Criterio verificable:** Una modificacion funcional en un componente no genera cambios en componentes dependientes.

## 4. Comunicacion confiable

Los procesos del sistema deben comunicarse de forma ordenada y consistente. Los eventos deben respetar el orden causal entre componentes.

**Criterio verificable:** El reloj logico de Lamport mantiene el orden causal de eventos entre sockets y gRPC.

## 5. Trazabilidad

Cada accion sobre una solicitud debe quedar registrada con un identificador temporal que permita reconstruir la secuencia de eventos.

**Criterio verificable:** Es posible reconstruir el historial completo de una solicitud a partir de los registros del sistema.

## 6. Fuentes

- **E3:** "los requisitos no funcionales" — uno de los 4 pilares obligatorios de la entrega E1.
- **E2, cap. 1.1.3:** justificacion distribuida como base para los RNF.
