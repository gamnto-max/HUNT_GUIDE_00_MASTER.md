# GUÍA MAESTRA DE DESPLIEGUE: PROCESADOR HUNT-TCU v1.2
## Paradigma Post-Data Center basado en el PEUO (Silicio-28)

Este documento coordina la inicialización secuencial del ecosistema. Cada módulo está numerado para garantizar que las dependencias de hardware (RTL) se carguen antes de los entornos de simulación y control (Python).

---

## 🗺️ Índice de Archivos del Ecosistema

### ⚡ Capa 1: Dimensión Material (Hardware RTL - Verilog)
*   **`HUNT_CORE_01_SPIN.v`**: Núcleo spintrónico que procesa la superposición de los espines electrónicos en la matriz de Silicio-28.
*   **`HUNT_TB_02_VAL.v`**: Banco de pruebas (Testbench) para inyectar vectores de fase y validar la inmunidad al ruido.

### 🕹️ Capa 2: Dimensión de Control (Software y Telemetría - Python)
*   **`HUNT_SIM_03_BLOCH.py`**: Simulador de la Esfera de Bloch y cálculo del índice de coherencia del PEUO en tiempo real.
*   **`HUNT_DASH_04_MONITOR.py`**: Interfaz unificada en Plotly Dash para visualizar la superposición atómica y la eficiencia energética de 0W.

---

## 🛠️ Instrucciones de Inicialización Secuencial

1. **Compilación del Hardware**: Ejecutar `HUNT_CORE_01_SPIN.v` en el software de síntesis (por ejemplo, Vivado o Quartus) para mapear las primitivas spint rónicas.
2. **Validación de Aserciones**: Correr la simulación con `HUNT_TB_02_VAL.v` para asegurar que el sistema no sufra descoherencia.
3. **Arranque del Panel**: Ejecutar `HUNT_DASH_04_MONITOR.py` para abrir la consola local de control.
