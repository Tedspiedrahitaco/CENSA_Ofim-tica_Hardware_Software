# 📖 Unidad 3: Arquitectura de Memoria y Gestión de Datos

La eficiencia de un sistema informático no se mide solo por la velocidad de procesamiento, sino por la velocidad y fiabilidad con la que puede acceder a los datos. Esta unidad explora la complejidad del subsistema de memoria.

## 1. La Jerarquía de Memoria del Sistema

La memoria no es un bloque monolítico; es una pirámide jerárquica diseñada para minimizar la latencia (retraso) entre la CPU y los datos.

### Nivel 0: Registros del Procesador
Almacenamiento microscópico dentro de los núcleos de la CPU. Son los datos que se están operando *en este ciclo de reloj*.
*   **Velocidad:** Instantánea (mismo ciclo de reloj).
*   **Capacidad:** Menos de 1 KB.

### Nivel 1, 2 y 3: Memoria Caché (SRAM)
Memoria Estática de Acceso Aleatorio. Es extremadamente rápida y costosa.
*   **L1:** Privada por núcleo. Divide instrucciones y datos.
*   **L2:** Privada por núcleo, más grande pero ligeramente más lenta.
*   **L3:** Compartida entre todos los núcleos. Sirve para sincronizar datos entre hilos.

### Nivel 4: Memoria Principal (DRAM)
Memoria Dinámica. Aquí residen los programas activos.
*   **DDR (Double Data Rate):** Transfiere datos tanto en la subida como en la bajada del ciclo de reloj, duplicando el ancho de banda efectivo.
*   **Timings y Latencia CAS (CL):** No solo importa la frecuencia (ej: 3200 MHz). La Latencia CAS (CL16, CL18) indica cuántos ciclos de reloj tarda la RAM en responder a una solicitud de la CPU. Una menor latencia es mejor.
    *   *Fórmula real de latencia (ns):* (CL / Frecuencia) * 2000.

---

## 2. Tecnologías de Protección y Rendimiento

### 2.1 ECC (Error Correcting Code)
Memoria crítica para servidores y estaciones de trabajo científicas. Posee un chip adicional que detecta y corrige errores de bit (Bit-flip) causados por radiación cósmica o interferencia magnética. Un solo bit errado en un banco podría corromper una transacción financiera millonaria.

### 2.2 Dual Channel / Quad Channel
Tecnología que duplica (o cuadruplica) el ancho de banda teórico al acceder a dos módulos de memoria simultáneamente. Para activarlo, los módulos deben instalarse en las ranuras correctas (generalmente A2 y B2) y ser idénticos en capacidad y velocidad.

---

## 3. Arquitectura de Almacenamiento Masivo

### 3.1 RAID (Redundant Array of Independent Disks)
Tecnología de virtualización de almacenamiento que combina múltiples discos físicos en una unidad lógica para mejorar redundancia, rendimiento o ambos.

*   **RAID 0 (Striping):** Suma la velocidad y capacidad de dos discos. Los datos se dividen entre ambos.
    *   *Ventaja:* Doble velocidad de lectura/escritura.
    *   *Riesgo Crítico:* Si falla un solo disco, se pierde TODA la información del arreglo. Indispensable tener backup externo.
*   **RAID 1 (Mirroring):** Crea un espejo exacto de los datos en dos discos.
    *   *Ventaja:* Alta redundancia. Si falla un disco, el sistema sigue funcionando.
    *   *Desventaja:* Se desperdicia el 50% de la capacidad total.
*   **RAID 5:** Requiere mínimo 3 discos. Usa paridad distribuida. Permite que falle un disco sin perder datos, pero la escritura es más lenta debido al cálculo de paridad.
*   **RAID 10 (1+0):** Un híbrido que ofrece la velocidad de RAID 0 y la seguridad de RAID 1. Requiere mínimo 4 discos. Es costoso pero ideal para bases de datos empresariales.

---

## 4. Sistemas de Archivos (File Systems)

Es la estructura lógica que el Sistema Operativo usa para organizar los datos en el disco. Sin un sistema de archivos, el disco es solo un mar de bits sin sentido.

### Windows
*   **NTFS (New Technology File System):** El estándar moderno. Soporta permisos de seguridad (ACL), archivos mayores a 4GB, compresión y encriptación.
*   **ExFAT:** Optimizado para memorias USB/SD. Compatible con Windows y Mac. Soporta archivos grandes pero no tiene la seguridad de NTFS.
*   **FAT32:** Obsoleto pero universal. No permite archivos de más de 4GB.

### Linux / Unix
*   **EXT4 (Fourth Extended Filesystem):** El estándar en la mayoría de distribuciones Linux. Robusto y reduce la fragmentación.
*   **Btrfs / ZFS:** Sistemas de nueva generación con "Self-healing" (autocuración) y snapshots nativos. Usados en servidores NAS.

### macOS
*   **APFS (Apple File System):** Optimizado para SSDs y cifrado nativo.

---

## 5. Cálculo Binario y Hexadecimal

El técnico debe entender cómo la máquina representa los datos internamente.

*   **Binario (Base 2):** 0 y 1.
*   **Decimal (Base 10):** 0 al 9.
*   **Hexadecimal (Base 16):** 0-9 y A-F. Se usa para direcciones de memoria y códigos de error porque compacta la información binaria (1 dígito hex = 4 bits).

**Conversión Práctica:**
Un byte (8 bits) puede ir de 00000000 (0) a 11111111 (255).
En Hexadecimal, esto va de 00 a FF. Por eso los colores RGB en diseño web van de #000000 (Negro) a #FFFFFF (Blanco).
