# 📖 Unidad 3: Arquitectura de Memoria y Gestión de Datos

La eficiencia de un sistema informático no se mide solo por la velocidad de procesamiento, sino por la velocidad y fiabilidad con la que puede acceder a los datos. Esta unidad explora la complejidad del subsistema de memoria.

## 1. Tipos de Memoria: RAM vs ROM

### 1.1 Memoria RAM (Random Access Memory)
Es la memoria de trabajo temporal.
*   **Analogía:** Una mesa de trabajo. Mientras más grande sea la mesa (8GB, 16GB, 32GB), más libros (programas) puedes tener abiertos simultáneamente sin que se caigan al suelo.
*   **Volátil:** Se borra al apagar el equipo.

### 1.2 Memoria ROM (Read Only Memory)
Es la memoria de solo lectura que contiene las instrucciones de inicio vitales.
*   **Analogía:** El "instinto de supervivencia" del computador. Es lo que sabe "al nacer" (BIOS/UEFI) antes de aprender nada (Instalar Windows). Permite que el equipo reconozca el teclado y el disco duro para arrancar.
*   **No Volátil:** No se borra sin electricidad.

---

## 2. La Jerarquía de Memoria del Sistema

La memoria no es un bloque monolítico; es una pirámide jerárquica diseñada para minimizar la latencia.

### Nivel 0: Registros del Procesador (~1 KB)
Datos inmediatos dentro de la CPU.

### Nivel 1, 2 y 3: Memoria Caché (SRAM)
Memoria Estática ultra-rápida. L1, L2 y L3 ayudan a que el procesador no tenga que esperar a la RAM lenta.

### Nivel 4: Memoria Principal (DRAM)
Aquí residen los programas activos. Se clasifica por generaciones (DDR3, DDR4, DDR5), cada una más rápida y eficiente energéticamente que la anterior. No son compatibles físicamente entre sí (la muesca cambia).

---

## 3. Unidades de Medida y Conversión

Para entender el almacenamiento, debemos hablar el lenguaje de las máquinas.

### 3.1 El Bit y el Byte
*   **Bit (b):** La unidad mínima (0 o 1). Un interruptor encendido o apagado.
*   **Byte (B):** 8 Bits. Equivale aproximadamente a una letra o carácter.

### 3.2 La Regla del 1024
En informática, usamos potencias de 2 ($2^{10} = 1024$).
*   1 **Kilobyte (KB)** = 1024 Bytes (Una página de texto).
*   1 **Megabyte (MB)** = 1024 KB (Una canción MP3).
*   1 **Gigabyte (GB)** = 1024 MB (Una película HD).
*   1 **Terabyte (TB)** = 1024 GB (Un disco duro moderno).

**Truco de Conversión:**
*   Para bajar (de GB a MB): **Multiplicar** por 1024.
*   Para subir (de MB a GB): **Dividir** por 1024.

### 3.3 Velocidad de Procesamiento (Hertz)
Los Hertz (Hz) miden la frecuencia de reloj, o los "latidos del corazón" del procesador.
*   **1 Hertz:** Un ciclo por segundo.
*   **1 Megahertz (MHz):** Un millón de ciclos por segundo.
*   **1 Gigahertz (GHz):** Mil millones de ciclos por segundo.
Un CPU de 3.5 GHz late 3,500,000,000 veces cada segundo.

---

## 4. Arquitectura de Almacenamiento Masivo

### 4.1 RAID (Redundant Array of Independent Disks)
*   **RAID 0:** Suma velocidad (Striping). Peligroso si falla un disco.
*   **RAID 1:** Espejo (Mirroring). Seguridad total, costoso.
*   **RAID 5:** Balance entre seguridad y costo.

## 5. Sistemas de Archivos (File Systems)
La estructura lógica del disco.
*   **Windows:** NTFS (Seguro), ExFAT (Compatible).
*   **Linux:** EXT4.
*   **Mac:** APFS.

---

## 6. Ofimática Básica: Microsoft PowerPoint

El objetivo de una presentación es **apoyar** al orador, no reemplazarlo.

### 6.1 Regla 10-20-30 (Guy Kawasaki)
*   **10 deapositivas:** No aburras a la audiencia.
*   **20 minutos:** Deja tiempo para preguntas.
*   **30 puntos de fuente:** Si la letra es pequeña, la gente lee en lugar de escucharte.

### 6.2 Elementos Visuales
*   **Imágenes:** "Una imagen vale más que mil palabras". Usa imágenes de alta calidad, no pixeladas.
*   **SmartArt:** Convierte listas de viñetas aburridas en diagramas de procesos o jerarquías visuales atractivas.

### 6.3 Transiciones y Animaciones
Úsalas con moderación.
*   **Transición:** Efecto al cambiar de diapositiva (Ej: Desvanecer).
*   **Animación:** Efecto dentro de la diapositiva (Ej: Que aparezca un texto).
*   *Consejo:* Evita efectos mareantes o ruidosos. La sobriedad comunica profesionalismo.
