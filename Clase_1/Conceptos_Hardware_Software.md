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
*   **Actualidad - Inteligencia Artificial:** Pasamos de procesar datos a procesar conocimiento. Las redes neuronales y el aprendizaje automático marcan la nueva era post-silicio.

---

## 3. Hardware y Software: La Simbiosis Perfecta

Una computadora es una unidad funcional compuesta por dos dimensiones inseparables.

> **Analogía Fundamental:**
> Un auto de Fórmula 1 (**Hardware**) sin un piloto experto (**Software**) es solo un trozo costoso de metal y fibra de carbono. El hardware proporciona la potencia bruta, pero el software proporciona la inteligencia y el control para usar esa potencia.

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

1.  **Supercomputadoras:** Sistemas de alto rendimiento (HPC) para cálculos científicos masivos.
2.  **Mainframes:** Computadoras centrales para grandes volúmenes de transacciones (Banca).
3.  **Workstations:** PCs de escritorio con hardware de grado empresarial para diseño y renderizado.
4.  **Computadoras Personales (PC):** Equipos de propósito general (Desktops, Laptops).
5.  **Microcontroladores / Sistemas Embebidos:** Pequeñas computadoras integradas en dispositivos cotidianos (IoT).

---

## 5. Green IT: Responsabilidad Ambiental

El avance tecnológico genera un desafío ecológico masivo.
*   **RAEE (Residuos de Aparatos Eléctricos y Electrónicos):** La "basura electrónica" contiene metales pesados (plomo, mercurio, cadmio) que contaminan el suelo y el agua si no se reciclan correctamente.
*   **Componentes Degradables:** La industria avanza hacia el uso de bioplásticos y soldaduras libres de plomo (RoHS) para minimizar el impacto.
*   **Eficiencia Energética:** El diseño moderno busca el máximo rendimiento por Watt consumido para reducir la huella de carbono de los centros de datos.

---

## 6. Ofimática Básica: Microsoft Word (Fundamentos)

El procesador de texto es la herramienta fundamental de la oficina moderna.

### 6.1 La Interfaz: Cinta de Opciones (Ribbon)
Microsoft Word organiza sus herramientas en pestañas lógicas:
*   **Inicio:** Herramientas más usadas (Fuente, Párrafo, Estilos).
*   **Insertar:** Para agregar elementos externos (Imágenes, Tablas, Gráficos).
*   **Diseño/Disposición:** Configuración de la página (Márgenes, Orientación).

### 6.2 Formato de Texto
La legibilidad es clave.
*   **Fuente:** Tipo de letra (Arial, Calibri). Títulos en 14pt-16pt, cuerpo en 11pt-12pt.
*   **Negrita (Ctrl+N):** Para resaltar conceptos clave, no párrafos enteros.
*   **Cursiva (Ctrl+K):** Para términos extranjeros o citas.

### 6.3 Guardado Correcto
*   **Guardar (Ctrl+G):** Mantiene el formato editable (.docx).
*   **Exportar a PDF:** Crea un documento de "solo lectura" universal, ideal para enviar hojas de vida o cotizaciones finales.
