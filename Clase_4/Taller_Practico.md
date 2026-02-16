# 📝 Taller Práctico 4: Desarrollo de Soluciones Empresariales

**Nivel de Complejidad:** Profesional
**Duración:** 120 Minutos
**Herramientas:** Microsoft Excel (Habilitado para Macros) y Microsoft Word.

---

## 🏢 Escenario: "Finanzas y Proyecciones LATAM"

Usted es el Analista de Datos Senior de una financiera. La gerencia regional le entrega un archivo plano (`ventas_anuales.csv`) con **10,000 registros** de transacciones. Los datos están sucios y desorganizados.

Se requiere una solución integral que automatice el reporte mensual y genere cartas de cobro a clientes morosos.

---

## 📊 Fase 1: ETL y Modelado de Datos (Excel)

1.  **Limpieza Avanzada:**
    *   Los nombres de los clientes vienen con espacios erróneos (Ej: "  JUAN   PEREZ  "). Use funciones anidadas (`ESPACIOS`, `NOMPROPIO`) para corregirlos.
    *   Genere un `Código Único` para cada transacción concatenando las primeras 3 letras de la Región, el Año y el ID numérico.

2.  **Lógica de Negocios (KPIs):**
    *   Cree una columna "Estado de Cartera" usando una función **SI Anidada compleja**:
        *   Si Días Mora > 90 -> "Jurídico"
        *   Si Días Mora > 60 -> "Pre-Jurídico"
        *   Si Días Mora > 30 -> "Riesgo Medio"
        *   Si no -> "Al Día"
    *   Cree una columna "Comisión Asesor" usando **BUSCARX** desde una tabla auxiliar de rangos de comisiones.

---

## 📈 Fase 2: Dashboard Interactivo

En una hoja nueva llamada "DASHBOARD" (sin celdas visibles, fondo gris profesional), construya:

1.  **Tablas Dinámicas Vinculadas:**
    *   Total Cartera por Región.
    *   Top 5 Clientes en Mora (Filtro de Top 10).
    *   Tendencia de Recaudo Mensual (Línea de tiempo).

2.  **Slicers (Segmentación de Datos):**
    *   Inserte botones para filtrar todo el reporte por: "Año", "Asesor" y "Tipo de Producto".

---

## 🤖 Fase 3: Automatización VBA (Macro)

La gerencia necesita un botón para exportar el reporte a PDF y limpiar los filtros.

1.  **Grabar Macro:** Grabe la acción de limpiar todos los filtros de los Slicers.
2.  **Edición de Código (VBA):**
    *   Entre al editor de VBA (Alt+F11).
    *   Modifique el código grabado para agregar un `MsgBox` al final que diga: "Reporte reiniciado exitosamente".
    *   Agregue una línea de código para que seleccione la celda A1 automáticamente al finalizar.

---

## ✉️ Fase 4: Integración Word-Excel (Mail Merge)

Se deben enviar cartas físicas a los clientes en estado "Jurídico".

1.  En Excel, filtre la base de datos para mostrar solo clientes "Jurídico" y copie esos datos a una nueva hoja llamada "Base_Cobros".
2.  En Word, redacte una "Carta de Notificación Pre-Legal".
3.  Utilice la herramienta **Correspondencia** para vincular el Excel.
4.  Inserte los campos combinados: `<<Nombre Cliente>>`, `<<Deuda Total>>`, `<<Días Mora>>`.
5.  Genere el documento final ("Finalizar y Combinar") creando un archivo nuevo con todas las cartas listas para imprimir.

---

## ✅ Rúbrica de Evaluación

*   **Excel (40%):** Funciones anidadas correctas y Dashboard funcional con Slicers conectados a todas las gráficas.
*   **VBA (30%):** El código no es solo grabado; muestra evidencia de edición manual (MsgBox, limpieza de variables).
*   **Integración (30%):** La combinación de correspondencia funciona y los campos coinciden con la base de datos filtrada.
*   **Bonus (+0.5):** Si el Dashboard incluye un gráfico de Mapa (Excel Maps) funcional.
