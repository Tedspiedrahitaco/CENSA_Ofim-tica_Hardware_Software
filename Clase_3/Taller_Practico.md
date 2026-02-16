# 📝 Taller Práctico 3: Gestión de Datos y Arquitectura de Sistemas

**Nivel de Complejidad:** Experto
**Duración:** 90 Minutos
**Herramientas:** Calculadora Binaria (Papel), Calculadora de RAID (Conceptos).

---

## 💾 Módulo 1: Diseño de Almacenamiento Empresarial (RAID)

Una empresa de post-producción de video 8K le contrata para diseñar su servidor de almacenamiento (NAS).
Requieren almacenar **40 TB** de material crudo.
La prioridad es:
1.  **Velocidad:** Necesitan leer a más de 1000 MB/s.
2.  **Seguridad:** No pueden permitirse perder datos si falla un disco.

**Discos Disponibles:**
Unidades NAS de 8 TB (Precio: $200 USD c/u).

**Cálculos a Realizar:**
1.  **Escenario RAID 0:**
    *   ¿Cuántos discos mínimos necesitan para llegar a 40 TB?
    *   ¿Cuál sería la velocidad teórica de lectura?
    *   ¿Cuál es el riesgo porcentual de fallo comparado con un solo disco? (Justifique por qué se descarta esta opción).
2.  **Escenario RAID 5:**
    *   ¿Cuántos discos necesitan para tener 40 TB *utilizables* (recuerde que se pierde la capacidad de 1 disco por paridad)?
    *   Costo total de la solución.
3.  **Escenario RAID 10:**
    *   ¿Cuántos discos necesitan para tener 40 TB *utilizables* (recuerde que se pierde el 50% por espejo)?
    *   Costo total de la solución.
    *   ¿Por qué esta opción es más rápida en escritura que el RAID 5?

**Decisión Final:**
Recomiende la mejor configuración balanceando Costo/Seguridad/Velocidad para este cliente específico y explique su elección.

---

## 🔢 Módulo 2: Matemáticas Computacionales (Sin Calculadora)

El análisis de volcados de memoria (Memory Dumps) requiere fluidez en Hexadecimal.

### Ejercicio A: Traducción de Direcciones
Convierta las siguientes direcciones de memoria Hexadecimales a Decimal:
1.  `0x0A`
2.  `0xFF`
3.  `0x10` (¡Cuidado! No es 10).

### Ejercicio B: Traducción de Máscara de Subred
En redes, la máscara `255.255.255.0` es muy común.
Convierta cada octeto a Binario. Debería obtener una secuencia de unos seguidos de ceros.
`11111111.11111111.11111111.00000000`
Demuestre el procedimiento.

---

## 📂 Módulo 3: Sistemas de Archivos y Particionamiento

Un cliente le trae un Disco Duro Externo de 4 TB. Quiere usarlo para transferir archivos de video de 50 GB entre su Macbook Pro (macOS) y su PC Gamer (Windows 11).

1.  **Análisis de Compatibilidad:**
    *   ¿Qué pasa si lo formatea en NTFS? (¿Lo lee Mac? ¿Lo escribe Mac?).
    *   ¿Qué pasa si lo formatea en HFS+? (¿Lo lee Windows?).
    *   ¿Qué pasa si usa FAT32? (¿Puede copiar el archivo de 50 GB?).
2.  **Solución Técnica:**
    *   ¿Cuál es el sistema de archivos correcto para este escenario híbrido? (Justifique las ventajas de exFAT vs NTFS con drivers de terceros).
    *   Explique qué es el "Tamaño de Unidad de Asignación" (Cluster Size) al formatear. ¿Para archivos de video grandes, conviene un cluster pequeño (4KB) o grande (128KB)? ¿Por qué?

---

## ✅ Criterios de Evaluación
*   **Lógica RAID:** Entender la penalización de paridad y espejo.
*   **Precisión Matemática:** Conversiones exactas sin errores.
*   **Criterio de Sistemas de Archivos:** Entender las limitaciones de tamaño de archivo y compatibilidad cruzada de sistemas operativos.
