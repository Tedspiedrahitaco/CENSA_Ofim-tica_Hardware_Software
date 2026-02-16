# 📖 Unidad 2: Arquitectura de Hardware Avanzada

El técnico profesional no solo conoce las piezas, sino la arquitectura que las interconecta. Esta unidad profundiza en los estándares y protocolos modernos de hardware.

## 1. Factor de Forma y Estándares de Chasis

El "Factor de Forma" (Form Factor) define las dimensiones físicas, los puntos de anclaje y la disposición eléctrica de los componentes.

### 1.1 Estándares ATX (Advanced Technology eXtended)
Desarrollado por Intel en 1995, sigue siendo el estándar dominante.
*   **E-ATX (Extended ATX):** (305 × 330 mm). Destinado a estaciones de trabajo y servidores. Soporta múltiples sockets de CPU y hasta 8 ranuras de RAM.
*   **ATX Estándar:** (305 × 244 mm). El más común. Ofrece equilibrio entre expansión (7 ranuras PCIe) y tamaño.
*   **Micro-ATX (mATX):** (244 × 244 mm). Mantiene el ancho pero reduce la altura (4 ranuras PCIe). Ideal para PCs de oficina compactos.
*   **Mini-ITX:** (170 × 170 mm). Diseñado para sistemas embebidos o HTPC (Home Theater PC). Solo posee 1 ranura PCIe. Su diseño térmico es crítico debido a la alta densidad de componentes.

## 2. La Placa Base (Motherboard): Anatomía Profunda

### 2.1 El Chipset y el PCH
Antiguamente, la placa tenía dos chips principales: Northbridge (Ram/Video) y Southbridge (USB/Audio).
En la arquitectura moderna (Intel/AMD), el Northbridge ha sido absorbido por la CPU, quedando solo el **PCH (Platform Controller Hub)**.
*   **Funciones del PCH:** Gestiona puertos SATA, USB, Audio HD, LAN y carriles PCIe secundarios.
*   **Bus DMI/Infinity Fabric:** Es el canal de comunicación ultra rápido que une la CPU con el PCH. Si este bus se satura, todo el sistema se ralentiza.

### 2.2 Fases de Alimentación (VRM)
Los **Módulos Reguladores de Voltaje (VRM)** son críticos para la estabilidad. Convierten los 12V de la fuente a los 1.1V - 1.4V que necesita la CPU.
*   Una placa base "barata" con pocas fases de VRM se sobrecalentará si instalamos un procesador de gama alta (i7/i9), causando *Thermal Throttling*.

## 3. Interfaces de Almacenamiento: Protocolos y Conectores

Es vital distinguir entre el *conector* físico y el *protocolo* lógico.

### 3.1 SATA (Serial ATA)
*   **SATA III:** Ancho de banda máximo teórico de 6 Gbps (aprox. 550 MB/s reales).
*   Limitante: Fue diseñado para discos mecánicos, por lo que frena el potencial de los chips Flash modernos.

### 3.2 NVMe (Non-Volatile Memory Express)
Protocolo diseñado específicamente para almacenamiento sólido (SSD), utilizando los carriles PCI Express.
*   **PCIe 3.0 x4:** ~3,500 MB/s.
*   **PCIe 4.0 x4:** ~7,500 MB/s.
*   **PCIe 5.0 x4:** ~14,000 MB/s. (Requiere disipadores de calor masivos).

### 3.3 Formato M.2
Es el conector físico. Puede alojar tanto discos SATA (lentos) como NVMe (rápidos).
*   **Key M vs Key B:** Muescas físicas en el conector que impiden insertar un disco incompatible.

## 4. Puertos y Conectividad Periférica

### 4.1 USB (Universal Serial Bus) - La Confusión de Nombres
El estándar USB ha sufrido múltiples renombramientos confusos:
*   **USB 3.0 / 3.1 Gen 1 / 3.2 Gen 1:** Velocidad de 5 Gbps. (Conector azul).
*   **USB 3.1 Gen 2 / 3.2 Gen 2:** Velocidad de 10 Gbps. (Conector rojo/teal).
*   **USB 3.2 Gen 2x2:** Velocidad de 20 Gbps. (Solo USB-C).
*   **USB4:** Hasta 40 Gbps, basado en Thunderbolt 3.

### 4.2 Thunderbolt
Propiedad de Intel/Apple. Combina datos (PCIe), video (DisplayPort) y energía (PD) en un solo cable. Permite conectar tarjetas gráficas externas (eGPU) a un portátil.

## 5. Fuentes de Poder (PSU) y Eficiencia Energética

No todos los Watts son iguales. La certificación **80 PLUS** garantiza la eficiencia de conversión energética (AC a DC).
*   **White:** 80% eficiencia.
*   **Bronze:** 82% eficiencia.
*   **Gold:** 87% eficiencia. (El estándar recomendado para equipos profesionales).
*   **Platinum/Titanium:** >90% eficiencia. (Servidores/Minería).

Una fuente de mala calidad puede entregar voltaje inestable ("Rizado" o *Ripple*), lo que degrada la vida útil de los capacitores de la placa base y la tarjeta gráfica, llevando a fallos prematuros.
