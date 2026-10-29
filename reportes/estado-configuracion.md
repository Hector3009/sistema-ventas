# Reporte de estado de configuración

Proyecto: Sistema de Ventas

Solicitud: CAM-002

Cambio: 10 % a 15 %

Issue: #1 — https://github.com/Hector3009/sistema-ventas/issues/1

Pull Request: #2 — https://github.com/Hector3009/sistema-ventas/pull/2

Commit inicial de referencia: `348943f7c55832b8ff6be174c946fbafd83dbdf5` — https://github.com/Hector3009/sistema-ventas/commit/348943f7c55832b8ff6be174c946fbafd83dbdf5

Elementos afectados: EC-002, EC-003, EC-004 y pruebas

Estado de implementación: en rama (`change/CAM-002-descuento`, Pull Request abierta, sin merge a `main`)

Pruebas ejecutadas: sí — ejecutadas por el asistente de IA (Claude) en un entorno de nube el 2026-10-28 a las 21:16 (hora de Ciudad de México); el participante todavía no las ha ejecutado en su propio equipo.

Evidencia: `python -m unittest discover -s tests -v` sobre el commit `afdcba5` de la rama (Python 3.13.18): 4 pruebas ejecutadas, resultado OK. Prueba de control: las mismas pruebas contra el código de la referencia inicial (`348943f`, 10 %) dan `FAILED (failures=1)` en `test_descuento_15`, lo que confirma que las pruebas detectan el cambio.

Nueva línea base: pendiente de aprobación
