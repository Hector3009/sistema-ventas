# Plan de Administración de la Configuración

Proyecto: Sistema de Ventas

Versión: 0.9

Estado: Borrador completo para revisión

## 1. Introducción y alcance
Este plan define reglas para identificar, controlar y verificar la configuración del Sistema de Ventas.

Incluye documentos, código, archivos de configuración, pruebas y registros de cambio.

## 2. Roles y responsabilidades
| Rol | Responsabilidad |
|---|---|
| Administrador de Configuración | Mantener el plan, inventario y registros de líneas base. |
| Administrador del Proyecto | Evaluar impactos y aprobar el plan conforme a su autoridad. |
| Asegurador de Calidad | Verificar evidencias y coordinar auditorías. |

## 3. Identificación de configuración
| ID | Elemento | Ruta |
|---|---|---|
| EC-001 | Plan SCM | docs/PLAN_SCM.md |
| EC-002 | Requisitos | docs/requisitos-descuentos.md |
| EC-003 | Configuración | config/descuentos.properties |
| EC-004 | Código | src/descuentos.py |

El Administrador de Configuración actualizará el inventario cuando se creen, cambien o retiren elementos.

## 4. Control de versiones
Documentos: versión X.Y y estado de elaboración, revisión o aprobación.

Código: commits para registrar cambios; ramas para desarrollarlos; Pull Requests para revisarlos; etiquetas vX.Y.Z para estados técnicos.

Una etiqueta no equivale a la aprobación formal de una línea base.

## 5. Líneas base
Cada línea base incluirá inventario, versiones, referencia Git, evidencia de revisión, responsable y estado de aprobación.

Referencia inicial: LB-VENTAS-001.

Comportamiento esperado: descuento máximo del 10 %.

Estado: referencia técnica; aprobación formal pendiente.

El commit exacto se registrará en el reporte de estado.

## 6. Librería de configuración
Repositorio: GitHub.

Carpetas: docs/, config/, src/, tests/, reportes/, auditorias/.

Acceso: conforme a los roles autorizados.

Cambios: mediante ramas y revisión de Pull Requests.

Respaldos: se definirán periodicidad, ubicación, responsable y prueba de recuperación. El historial Git no sustituye respaldos.

## 7. Control de cambios
1. Registrar solicitud mediante Issue.
2. Evaluar impacto y riesgos.
3. Autorizar o rechazar formalmente.
4. Planear e implementar en rama.
5. Verificar requisitos y pruebas.
6. Revisar mediante Pull Request.
7. Integrar según criterios aprobados.
8. Actualizar inventario, reportes y línea base.

Una implementación técnica no significa liberación aprobada.

## 8. Reportes de estado
Se reportarán inventario, versiones, líneas base, solicitudes, Pull Requests, pruebas, permisos y hallazgos de auditoría.

Cada reporte incluirá evidencia verificable y estado actualizado.

## 9. Auditorías
Auditoría física: revisar existencia, integridad, identificación y correspondencia de los elementos.

Auditoría funcional: verificar evidencia de requisitos y pruebas.

El Asegurador de Calidad documentará hallazgos y seguimiento.

No se aprobará una línea base sin cumplir criterios definidos.

## 10. Calendario y herramientas
Inicio: elaborar el plan e identificar elementos.

Desarrollo: registrar versiones y controlar cambios.

Antes de línea base: revisar elementos y evidencias.

Antes de entrega: realizar auditoría.

Cierre: emitir reporte de estado.

Herramientas: GitHub, Issues, ramas, commits y Pull Requests.
