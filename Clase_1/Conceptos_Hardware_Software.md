# 📖 Unidad 1: Fundamentos de Sistemas, Hardware y Software

## 1. Introducción a la Teoría General de Sistemas

La **Teoría General de Sistemas (TGS)**, propuesta por el biólogo Ludwig von Bertalanffy, establece que un sistema es un conjunto de elementos que interactúan entre sí para lograr un objetivo común. En el contexto informático, esta definición es literal y estricta. Un sistema computacional no es una máquina aislada, sino una integración compleja de hardware, software, datos y factor humano.

### 1.1 El Ciclo de Procesamiento de Información (IPOS)
Todo sistema computacional, independientemente de su potencia o tamaño, opera bajo el ciclo **IPOS** (Input -> Process -> Output -> Storage).

1.  **Entrada (Input):** Es la fase de recolección de datos no procesados. Los dispositivos de entrada convierten señales físicas (teclas pulsadas, movimientos del mouse, ondas sonoras) en señales digitales (binarias) que el sistema puede interpretar.
2.  **Procesamiento (Process):** Es el corazón del sistema. La Unidad Central de Procesamiento (CPU) ejecuta instrucciones lógicas y aritméticas sobre los datos de entrada. Aquí es donde los datos crudos se transforman en *información* significativa.
3.  **Salida (Output):** La información procesada se presenta al usuario en un formato comprensible (visual, auditivo, impreso). Es la decodificación de los datos binarios a lenguaje humano.
4.  **Almacenamiento (Storage):** Dado que la memoria de trabajo (RAM) es volátil, el sistema requiere medios de persistencia para guardar los resultados del procesamiento de manera segura a largo plazo.

---

## 2. Historia de la Computación: Hitos Técnicos

La evolución del cómputo no fue lineal, sino exponencial.

*   **1642 - La Pascalina:** Blaise Pascal inventa la primera calculadora mecánica basada en engranajes y ruedas dentadas. Aunque limitada a sumas y restas, demostró que una máquina podía "calcular".
*   **1837 - La Máquina Analítica:** Charles Babbage diseña teóricamente una máquina programable con unidad de memoria y procesador. Es el primer diseño de una computadora de propósito general.
*   **1945 - Arquitectura de Von Neumann:** John von Neumann describe la arquitectura que usan casi todas las computadoras modernas: una unidad de procesamiento y una memoria donde se almacenan *tanto* los datos como las instrucciones del programa. Antes de esto, reprogramar una computadora implicaba recablear físicamente sus circuitos.
*   **1947 - El Transistor:** Inventado en los Laboratorios Bell. Reemplazó a los voluminosos y calientes tubos de vacío, permitiendo la miniaturización y fiabilidad electrónica.
*   **1971 - Intel 4004:** El primer microprocesador en un solo chip. Marcó el inicio de la era de la Computación Personal (PC).

---

## 3. Hardware y Software: Definiciones Técnicas

### 3.1 Hardware (Infraestructura Física)
Se refiere a la totalidad de componentes físicos del sistema. Se clasifica en:
*   **Hardware de Procesamiento:** CPU, GPU (Unidad de Procesamiento Gráfico).
*   **Hardware de Almacenamiento:** Discos Duros (HDD), Estados Sólidos (SSD), Memorias Flash.
*   **Hardware de Entrada/Salida:** Periféricos que permiten la comunicación bidireccional hombre-máquina.

**La Ley de Moore:**
Gordon Moore predijo empíricamente que el número de transistores en un circuito integrado denso se duplicaría aproximadamente cada dos años. Esto explica por qué el hardware se vuelve obsoleto tan rápido y su potencia crece exponencialmente.

### 3.2 Software (Infraestructura Lógica)
Es el conjunto de instrucciones codificadas que controlan el funcionamiento del hardware. Sin software, el hardware es inerte ("Metal muerto").

#### Clasificación del Software:
1.  **Software de Sistema:** Es la base que permite al hardware funcionar. Incluye el Sistema Operativo (Windows, Linux, macOS), los controladores de dispositivos (Drivers) y las utilidades de diagnóstico. Su función es abstraer la complejidad del hardware para el usuario y las aplicaciones.
2.  **Software de Aplicación:** Programas diseñados para realizar tareas específicas para el usuario final (Navegadores, Procesadores de Texto, Videojuegos, CRM).
3.  **Software de Programación:** Herramientas que permiten a los desarrolladores escribir, depurar y mantener otros programas (Compiladores, IDEs, Intérpretes).

#### Tipos de Licenciamiento:
*   **Software Propietario (Copyright):** El código fuente es cerrado. El usuario paga por el derecho de uso (Licencia), pero no es dueño del software. (Ej: Microsoft Office).
*   **Software Libre (Copyleft / GPL):** El usuario tiene libertad para ejecutar, copiar, distribuir, estudiar, cambiar y mejorar el software. (Ej: Kernel Linux).
*   **Freeware:** Software gratuito pero de código cerrado.
*   **Shareware:** Software de prueba gratuito por tiempo limitado.

---

## 4. Clasificación de Computadoras por Potencia

Más allá de "Laptop vs Escritorio", la industria clasifica los equipos por su capacidad de cómputo (FLOPS - Operaciones de Coma Flotante por Segundo).

1.  **Supercomputadoras:**
    *   Sistemas de alto rendimiento (HPC) diseñados para cálculos científicos masivos (clima, física nuclear, modelado genético). No usan un solo procesador, sino miles trabajando en paralelo (Clústers).
    *   *Ejemplo:* Frontier, Fugaku.

2.  **Mainframes:**
    *   Computadoras centrales diseñadas para procesar millones de transacciones simultáneas con una fiabilidad del 99.999%. Priorizan el volumen de datos de entrada/salida (I/O) sobre el cálculo puro.
    *   *Uso:* Banca, Aerolíneas, Censos gubernamentales.

3.  **Workstations (Estaciones de Trabajo):**
    *   PCs de escritorio con hardware de grado empresarial (Memoria ECC, CPUs Xeon/Threadripper, GPUs Quadro). Diseñadas para tareas críticas como renderizado 3D, edición de video 4K o análisis de ingeniería (CAD/CAM).

4.  **Computadoras Personales (PC):**
    *   Equipos de propósito general para usuarios finales. Incluye Desktops, Laptops, Tablets y Smartphones (sí, tu teléfono es una computadora poderosa).

5.  **Microcontroladores / Sistemas Embebidos:**
    *   Pequeñas computadoras integradas dentro de otros dispositivos (Lavadoras, Semáforos, Autos, Sistemas de Alarma). Tienen recursos muy limitados y ejecutan una sola tarea específica en tiempo real.
