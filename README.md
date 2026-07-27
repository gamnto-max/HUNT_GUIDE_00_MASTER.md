# Procesador HUNT-TCU v1.2: Ecosistema Spintrónico Basado en el PEUO

Este repositorio contiene la implementación del núcleo de procesamiento **HUNT-TCU v1.2** fundamentado en el **Principio de Equivalencia Universal Ondulatorio (PEUO)**. Al utilizar la superposición de los espines de los electrones en sustratos ultra-puros de **Silicio-28**, este paradigma elimina la dependencia de infraestructuras centralizadas y de alta disipación térmica, proponiendo una alternativa directa a los Data Centers convencionales.

---

## 🏗️ Arquitectura del Repositorio

El proyecto está estructurado con una nomenclatura indexada numéricamente para forzar un despliegue secuencial correcto:

```text
PROCESADORHUNT/
├── README.md                      # Este archivo de diagnóstico e inducción.
├── HUNT_GUIDE_00_MASTER.md        # Hoja de ruta técnica de archivos.
├── hardware/
│   ├── HUNT_CORE_01_SPIN.v        # Archivo RTL del núcleo en Verilog.
│   └── HUNT_TB_02_VAL.v          # Banco de pruebas (Testbench).
└── software/
    ├── HUNT_SIM_03_BLOCH.py       # Algoritmo matemático del estado de espín.
    └── HUNT_DASH_04_MONITOR.py    # Interfaz de telemetría y consola en Dash.
```

---

## 🛠️ Requisitos de Entorno

### ⚡ Entorno de Hardware (Simulación RTL)
*   **Simulador Verilog**: Icarus Verilog (iverilog), ModelSim, Vivado Simulator o EDA PlayGround.
*   **Visualizador de Ondas**: GTKWave (para inspección de transiciones lógicas).

### 🕹️ Entorno de Software (Control y Telemetría)
*   **Python**: Versión 3.8 o superior.
*   **Librerías Requeridas**:
    ```bash
    pip install dash plotly numpy
    ```

---

## 🚀 Guía de Ejecución Rápida

### Paso 1: Validación del Hardware en Consola
Para compilar y verificar el comportamiento del núcleo spintrónico utilizando **Icarus Verilog**, ejecute los siguientes comandos en su terminal:

```bash
# 1. Compilar el núcleo junto a su banco de pruebas
iverilog -o hunt_system.vvp hardware/HUNT_CORE_01_SPIN.v hardware/HUNT_TB_02_VAL.v

# 2. Ejecutar la simulación lógica
vvp hunt_system.vvp
```

### Paso 2: Ejecución del Algoritmo Matemático de Espín
Valide los cálculos vectoriales de la esfera de Bloch en el intérprete de Python:

```bash
python software/HUNT_SIM_03_BLOCH.py
```

### Paso 3: Inicialización de la Consola de Monitoreo
Inicie el servidor local para visualizar el índice de coherencia en tiempo real en una interfaz gráfica interactiva:

```bash
python software/HUNT_DASH_04_MONITOR.py
```
*Una vez ejecutado, abra su navegador web e ingrese a la dirección local:* `http://127.0.0`

---

## 🔬 Premisas Técnicas para Auditoría de Fundición
*   **Aislamiento de Espín Nuclear**: El diseño asume la total ausencia de isótopos de Silicio-29 para evitar el ruido de acoplamiento hiperfino en la red atómica.
*   **Disipación Estática Cero**: Al basar el procesamiento en la orientación angular y no en el tránsito macroscópico de portadores de carga eléctrica, el módulo no genera pérdidas óhmicas caloríficas.
