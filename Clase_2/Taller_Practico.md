# 📝 Taller Práctico 2: Diagnóstico Avanzado y Arquitectura de Hardware

**Nivel de Complejidad:** Experto
**Duración:** 90 Minutos
**Herramientas:** Calculadora de PSU (Online u Offline), Manuales de Placa Base (PDF).

---

## 🔬 Módulo 1: Análisis Forense de Fallos

Analice los siguientes escenarios técnicos complejos. No se limite a la respuesta obvia; busque la causa raíz.

### Caso A: El "Reinicio Aleatorio"
Un PC Gamer con RTX 3080 y Core i9-12900K se apaga abruptamente *solo* cuando juega títulos exigentes en 4K. Navegando o editando Word funciona perfecto.
*   **Fuente instalada:** 600W 80 Plus White.
*   **Diagnóstico:** Calcule el consumo total del sistema (TDP de CPU + TDP de GPU + Otros). ¿Es suficiente la fuente?
*   **Hipótesis de Fallo:** Explique el concepto de "Pico Transitorio de Energía" (Transient Spike) de las GPUs modernas y por qué una fuente de 600W falla aunque el consumo promedio sea de 550W.

### Caso B: SSD "Lento"
Un cliente compró un SSD M.2 NVMe de 3500 MB/s. Lo instaló en su placa base antigua (chipset Z97) usando un adaptador PCIe.
*   **Síntoma:** El test de velocidad muestra solo 1600 MB/s.
*   **Análisis:** Investigue las versiones de PCI Express. ¿Cuál es el ancho de banda máximo de un puerto PCIe 2.0 x4 vs PCIe 3.0 x4?
*   **Conclusión:** ¿El disco está defectuoso o es un cuello de botella de la interfaz?

---

## 🛠️ Módulo 2: Ingeniería de Actualización (Upgrade)

Tiene un servidor antiguo con las siguientes especificaciones:
*   **Placa:** ASUS P8Z77-V LK (Socket 1155).
*   **CPU:** Core i5-3570K.
*   **RAM:** 8GB DDR3 1333 MHz.

El cliente quiere usarlo para **Edición de Video 4K**.
1.  Investigue la lista de compatibilidad de CPU (QVL) de esa placa específica. ¿Cuál es el procesador más potente que soporta?
2.  ¿Soporta memoria RAM DDR4? (Justifique técnicamente por qué física y eléctricamente no es compatible).
3.  ¿Tiene ranura para M.2 NVMe nativo? Si no, ¿cómo conectaría almacenamiento rápido de forma booteable? (Esto requiere investigar sobre modificación de BIOS o arranque por Legacy ROM).

---

## 📐 Módulo 3: Cálculo de Cuello de Botella (Bottleneck)

Usted debe armar un presupuesto equilibrado. Explique con porcentajes estimados de pérdida de rendimiento los siguientes emparejamientos:

1.  **Escenario 1:** CPU Celeron G5905 + GPU NVIDIA RTX 4090.
    *   ¿Quién frena a quién?
    *   ¿Por qué ocurre el frenado? (Explique el ciclo de renderizado CPU -> GPU).

2.  **Escenario 2:** CPU Ryzen 9 7950X + GPU GT 710.
    *   ¿Esta configuración tiene sentido para una Workstation de Compilación de Código? (Sí/No y Por qué).

---

## 🔌 Módulo 4: Identificación Visual de Puertos

(El profesor mostrará imágenes de puertos físicos o mostrará la placa base real).
Identifique y describa la función técnica de:
1.  Header USB 3.0 (19 pines).
2.  Header RGB (4 pines 12V) vs ARGB (3 pines 5V). **Advertencia:** Explique qué pasa si conecta una tira LED de 5V en el conector de 12V.
3.  Conector EPS de 8 pines (CPU) vs Conector PCIe de 8 pines (GPU). ¿Son intercambiables? (Analice la forma de los pines "Keying").

---

## ✅ Criterios de Evaluación
*   **Precisión Técnica:** Uso correcto de términos (Watts, Amperios, Bandwidth, Lanes).
*   **Seguridad:** Identificar correctamente los riesgos eléctricos (RGB 5V vs 12V, EPS vs PCIe).
*   **Lógica de Diagnóstico:** Capacidad para aislar variables en los casos de fallo.
