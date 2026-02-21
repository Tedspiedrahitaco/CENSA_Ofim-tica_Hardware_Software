# 📖 Unidad 2: Arquitectura de Hardware Avanzada

El técnico profesional no solo conoce las piezas, sino la arquitectura que las interconecta. Esta unidad profundiza en los estándares y protocolos modernos de hardware.

## 1. Factor de Forma y Estándares de Chasis

El "Factor de Forma" (Form Factor) define las dimensiones físicas, los puntos de anclaje y la disposición eléctrica de los componentes.

### 1.1 Estándares ATX (Advanced Technology eXtended)
Desarrollado por Intel en 1995, sigue siendo el estándar dominante.
*   **E-ATX:** Para servidores. Soporta múltiples CPUs.
*   **ATX Estándar:** El más común. Equilibrio expansión/tamaño.
*   **Micro-ATX:** Compacto. Ideal oficinas.
*   **Mini-ITX:** (170x170mm). Para sistemas muy pequeños (HTPC).

## 2. La Placa Base (Motherboard): Anatomía Profunda

### 2.1 El Chipset y el PCH
El **Chipset** funciona como el sistema de carreteras de una ciudad.
*   **Funciones del PCH:** Gestiona puertos SATA, USB, Audio HD, LAN y carriles PCIe secundarios.
*   **Bus DMI:** Canal ultra rápido entre CPU y PCH.

### 2.2 Fases de Alimentación (VRM)
Módulos Reguladores de Voltaje. Convierten 12V a ~1.2V para la CPU. Es el "Corazón" eléctrico de la placa.

## 3. Interfaces de Almacenamiento y Particionamiento

Es vital distinguir entre el *conector* físico y el *protocolo* lógico.

### 3.1 Tecnologías Físicas
*   **HDD (Disco Duro):** Mecánico, platos magnéticos. Como un tocadiscos antiguo (Lento, económico, gran capacidad).
*   **SSD (Estado Sólido):** Chips de memoria. Como una memoria USB gigante (Rápido, resistente a golpes, más costoso por GB).
*   **NVMe:** Protocolo sobre PCIe para SSDs ultra-rápidos (>3500 MB/s).

### 3.2 Particionamiento de Discos
División lógica de una unidad física.
*   **Partición C: (Sistema):** Donde se instala Windows y Programas. Si falla, se puede formatear sin perder los documentos.
*   **Partición D: (Datos):** Donde el usuario guarda fotos, música, trabajos.
*   **Seguridad:** Mantener los datos separados del sistema operativo es la regla de oro del mantenimiento.

## 4. Puertos y Conectividad Periférica

### 4.1 USB (Universal Serial Bus)
*   **USB 3.0 / 3.1 / 3.2:** Diferentes velocidades (5, 10, 20 Gbps). Diferenciados por colores (Azul, Rojo).
*   **USB-C:** El conector reversible del futuro.

### 4.2 Dispositivos Híbridos (E/S)
No son solo entrada o salida, hacen ambas funciones.
*   **Pantallas Táctiles:** Muestran imagen (Salida) y reciben toques (Entrada).
*   **Routers/Módems:** Envían y reciben datos a internet.
*   **Headsets:** Tienen audífonos (Salida) y micrófono (Entrada).

## 5. Mantenimiento Preventivo Básico
La vida útil del PC depende de su cuidado.
*   **Gestión del Polvo:** El polvo actúa como aislante térmico y conductor eléctrico. Limpiar los filtros y ventiladores regularmente evita el sobrecalentamiento.
*   **Ubicación:** Nunca poner la torre directamente en alfombras (generan estática y bloquean flujo de aire). Elevarla del suelo al menos 10cm.
*   **Gestión de Cables:** Un interior ordenado mejora el flujo de aire.

## 6. Fuentes de Poder (PSU) y Eficiencia Energética

No todos los Watts son iguales. La certificación **80 PLUS** garantiza la eficiencia de conversión energética (AC a DC). Una fuente de mala calidad puede quemar todo el sistema.

---

## 7. Ofimática Básica: Microsoft Excel (Fundamentos)

Excel no es una calculadora, es un motor de análisis de datos.

### 7.1 Conceptos Anatómicos
*   **Libro:** El archivo completo (.xlsx).
*   **Hoja:** Las pestañas inferiores. Puedes tener múltiples hojas en un libro.
*   **Celda (Ej: B5):** La intersección única donde se guarda el dato.

### 7.2 Tipos de Datos
Excel necesita saber qué le estás escribiendo:
*   **General/Texto:** Nombres, descripciones. Se alinean a la izquierda.
*   **Número:** Cantidades. Se alinean a la derecha.
*   **Moneda:** Agrega el signo ($) y decimales. Vital para contabilidad.
*   **Fecha Corta:** (dd/mm/aaaa).

### 7.3 Operaciones Matemáticas Básicas
TODA fórmula en Excel empieza con un igual (`=`).
*   **Suma:** `=A1 + B1`
*   **Resta:** `=A1 - B1`
*   **Multiplicación:** `=A1 * B1` (No usar "x", usar asterisco).
*   **División:** `=A1 / B1` (Barra inclinada).
