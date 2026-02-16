# 📖 Unidad 4: Procesamiento Avanzado y Automatización Empresarial

Esta unidad es el puente entre la ingeniería de hardware pura y la aplicación práctica en el mundo de los negocios.

## 1. Arquitectura Interna del Microprocesador (CPU)

La CPU es un circuito integrado de complejidad inimaginable (miles de millones de transistores en nanómetros). Para entenderla, debemos mirar dentro de sus bloques funcionales.

### 1.1 Unidad Aritmético Lógica (ALU)
Es la calculadora real del procesador. Realiza operaciones matemáticas básicas (suma, resta, multiplicación) y lógicas (AND, OR, NOT, XOR). Todo lo que haces en la computadora, desde jugar hasta escribir un correo, se descompone en millones de estas operaciones simples.

### 1.2 Unidad de Control (CU)
Es el "Director de Tráfico". No procesa datos, sino que dirige el flujo de información. Decide qué datos van a la ALU, cuáles van a memoria y cuáles a los periféricos. Decodifica las instrucciones del programa y genera las señales de control para el resto de la CPU.

### 1.3 Registros
Son pequeñas celdas de memoria de ultra-alta velocidad (aún más rápidas que la Caché L1). Almacenan temporalmente los operandos y resultados de la ALU.
*   *Ejemplo:* Si sumas 5 + 3, el 5 se guarda en un registro, el 3 en otro, y el resultado 8 en un tercer registro acumulador.

### 1.4 Conjuntos de Instrucciones: CISC vs RISC
La filosofía de diseño del procesador define su eficiencia.
*   **CISC (Complex Instruction Set Computing):** (Ej: Intel x86, AMD64). Usa instrucciones complejas que pueden realizar múltiples operaciones en un solo ciclo. Potente pero consume más energía. Dominante en PCs y Servidores.
*   **RISC (Reduced Instruction Set Computing):** (Ej: ARM en celulares, Apple Silicon M1/M2/M3). Usa instrucciones muy simples y optimizadas. Requiere más código para hacer lo mismo, pero es extremadamente eficiente energéticamente. Dominante en móviles y dispositivos IoT.

---

## 2. Microsoft Excel: Lógica y Análisis de Datos (Data Analytics)

En un entorno corporativo, Excel se utiliza para limpiar, transformar y visualizar datos.

### 2.1 Funciones Lógicas Avanzadas
No basta con `SUMA` o `PROMEDIO`. El análisis requiere lógica condicional.
*   **SI Anidado (Nested IF):** Evaluar múltiples condiciones en cadena.
    *   `=SI(Venta>1000, "Bono Alto", SI(Venta>500, "Bono Medio", "Sin Bono"))`
*   **Y / O (AND / OR):** Conectores lógicos para evaluar varios criterios simultáneos.
    *   `=SI(Y(Venta>1000; Asistencia="Perfecta"); "Empleado del Mes"; "")`
*   **BUSCARX (XLOOKUP):** La evolución moderna de BUSCARV. Permite buscar en cualquier dirección, devolver matrices y manejar errores sin funciones adicionales.

### 2.2 Tablas Dinámicas (Pivot Tables)
Son herramientas de resumen multidimensional. Permiten "pivotar" (girar) los ejes de análisis.
*   *Ejemplo:* Convertir una lista plana de 50.000 ventas en una matriz que muestre Ventas por Región (Filas), por Categoría de Producto (Columnas) y filtrado por Año.
*   *Campos Calculados:* Crear nuevas métricas dentro de la tabla dinámica sin alterar la base de datos original (Ej: Calcular el Ticket Promedio = Ventas / Cantidad Transacciones).

---

## 3. Automatización con Macros y VBA

Cuando una tarea se repite más de 3 veces, debe automatizarse.

### 3.1 La Grabadora de Macros
Convierte tus acciones (clics, tecleo) en código VBA automáticamente. Es el primer paso para la automatización.
*   **Limitación:** Es rígida. Si los datos cambian de posición, la macro grabada fallará.

### 3.2 Visual Basic for Applications (VBA)
Es el lenguaje de programación detrás de Office. Permite crear lógica compleja que la grabadora no puede.
*   **Variables:** Almacenar valores temporales.
*   **Bucles (For / Loop):** Repetir una acción 1000 veces en segundos.
*   **InputBox / MsgBox:** Interactuar con el usuario pidiendo datos o mostrando alertas.

```vba
Sub SaludoCorporativo()
    Dim Nombre As String
    Nombre = InputBox("Ingrese su nombre:")
    If Nombre <> "" Then
        MsgBox "Bienvenido al Sistema, " & Nombre, vbInformation
    Else
        MsgBox "Error: Nombre requerido", vbCritical
    End If
End Sub
```

---

## 4. Microsoft Word: Documentación Técnica Estructurada

### 4.1 Secciones y Saltos
Un documento profesional no es un flujo continuo. Las "Secciones" permiten tener partes del documento con configuraciones independientes.
*   *Caso de Uso:* Tener la página 1 en Vertical (Portada), la página 2 en Horizontal (Tabla ancha) y la página 3 en Vertical de nuevo. Esto es imposible sin Saltos de Sección.

### 4.2 Combinación de Correspondencia (Mail Merge)
La integración entre Excel (Base de Datos) y Word (Plantilla).
Permite generar 500 cartas personalizadas o 500 certificados de asistencia en PDF en minutos, tomando los nombres y cédulas desde una lista de Excel.
