# Auditoría CAM-002

Auditoría física:
- Requisitos, configuración y código consistentes: sí (los tres indican 15 % en la rama `change/CAM-002-descuento`)
- Trazabilidad a Issue y PR: sí (Issue #1 y Pull Request #2)
- Inventario actualizado: no (el apartado 3 del plan no registra `tests/test_descuentos.py`, `reportes/` ni `auditorias/`)

Auditoría funcional:
- Pruebas definidas: sí (4 casos: 10 %, 15 %, 16 % y negativo)
- Ejecución demostrada: sí, por el asistente de IA en un entorno de nube; falta ejecución propia del participante
- Resultado: conforme (4 de 4 pruebas OK con el código de la rama)

Hallazgos:
1. Las pruebas y los reportes no están registrados como elementos de configuración en el inventario.
2. El cambio está implementado en rama y en revisión; no está integrado en `main`.
3. La evidencia de pruebas proviene del asistente de IA, no del participante.
4. `config/descuentos.properties` no es leído por el código; la consistencia del límite depende del proceso SCM.

Conclusión: pendiente

Aprobación de nueva línea base: pendiente
