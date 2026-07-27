# Procesador HUNT-TCU v1.2: Ecosistema Spintrónico Basado en el PEUO

Este repositorio contiene el código de producción, simulación lógica y telemetría interactiva del núcleo de procesamiento **HUNT-TCU v1.2** fundamentado en el **Teorema de Hunt** y el **Principio de Equivalencia Universal Ondulatorio (PEUO)**. 

Al emplear la superposición estática de espines electrónicos en sustratos de **Silicio-28 purificado**, esta arquitectura prescinde del movimiento de portadores de carga y de las pérdidas por disipación térmica, planteando una alternativa directa y local frente al modelo de Data Centers masivos.

---

## 🏗️ Estructura Secuencial del Repositorio

Para preservar de manera estricta el orden de inicialización y las dependencias, el proyecto sigue una nomenclatura indexada numéricamente:

```text
PROCESADORHUNT/
├── README.md                        # Este documento (Manual de inducción y auditoría).
├── HUNT_GUIDE_00_MASTER.md          # Índice y hoja de ruta técnica de archivos.
├── hardware/
│   ├── HUNT_CORE_01_SPIN.v          # Código RTL base del núcleo en Verilog.
│   ├── HUNT_TB_02_VAL.v            # Banco de pruebas (Testbench) para aserciones.
│   └── HUNT_GATE_06_SPIN.v          # Modelado de compuertas atómicas por fase (NUEVO).
└── software/
    └── streamlit_app.py             # Aplicación unificada para create.streamlit.app
                                     # (Integra los archivos 00, 03, 04, 05 y 07).
```

---

## 🛠️ Requisitos del Entorno de Validación

### ⚡ Simulación de Hardware (RTL)
*   **Simulador Verilog**: Icarus Verilog (`iverilog`), ModelSim o Vivado Simulator.
*   **Visualizador de Formas de Onda**: GTKWave (para verificar la estabilidad del bus cuántico).

### 🕹️ Simulación Visual e Impacto (Entorno en la Nube)
*   Despliegue directo a través de la interfaz web nativa en **`create.streamlit.app`**. Las dependencias analíticas (`streamlit`, `plotly`, `numpy`, `pandas`) son resueltas de forma automatizada por el contenedor en la nube.

---

## 🚀 Protocolo de Ejecución

### 1. Pruebas de Síntesis Lógica (Hardware local)
Mapee el comportamiento de las compuertas de espín y el bus cuántico compilando los módulos en consola:

```bash
# Compilar el núcleo de compuertas y el entorno de simulación
iverilog -o hunt_gate_system.vvp hardware/HUNT_GATE_06_SPIN.v hardware/HUNT_CORE_01_SPIN.v

# Ejecutar el binario lógico resultante
vvp hunt_gate_system.vvp
```

### 2. Pruebas de Telemetría Gráfica y Tiempos de Conmutación (Software)
Para auditar las proyecciones en la esfera de Bloch, los tiempos de retraso en attosegundos y los modelos de ahorro financiero, acceda a su aplicación web desplegada en Streamlit. Navegue utilizando el menú lateral interactivo siguiendo la numeración estricta de la guía maestra.

---

## 🔬 Especificaciones Fundamentales para Fundición Avanzada
*   **Eliminación del Acoplamiento Hiperfino**: Se requiere un entorno libre de isótopos de Silicio-29 (pureza > 99.999% de Si-28) para evitar la fluctuación magnética del espín nuclear.
*   **Anulación de Barreras RC**: Al eliminar la corriente macroscópica por líneas de cobre o aluminio, las limitaciones clásicas de resistencia y capacitancia parásita de los transistores desaparecen, permitiendo velocidades de reloj en el rango de transiciones ultra-rápidas.
