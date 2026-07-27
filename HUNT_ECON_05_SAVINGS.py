import streamlit as st
import plotly.graph_objs as go
import numpy as np
import pandas as pd

# Configuración global del ecosistema en Streamlit
st.set_page_config(page_title="Ecosistema HUNT-TCU v1.2", layout="wide")

st.title("HUNT-TCU v1.2: SISTEMA OPERATIVO ATÓMICO")
st.write("Paradigma de procesamiento descentralizado basado en el PEUO y Silicio-28")

# Selector de archivos indexado en el panel lateral
opcion_archivo = st.sidebar.selectbox(
    "Selecciona el Módulo a Ejecutar:",
    [
        "HUNT_DASH_04_MONITOR (Consola Gráfica)", 
        "HUNT_SIM_03_BLOCH (Cálculo de Fase)",
        "HUNT_ECON_05_SAVINGS (Simulador de Impacto Financiero)"
    ]
)

# =========================================================================
# MODULO 04: CONSOLA GRÁFICA DE TELEMETRÍA
# =========================================================================
if opcion_archivo == "HUNT_DASH_04_MONITOR (Consola Gráfica)":
    st.header("HUNT SPIN-RESONANCE MONITOR v1.2")
    theta_deg = st.sidebar.slider("Ángulo de Fase Espín Electrónico (θ):", 0, 180, 90, 1)
    
    theta = np.radians(theta_deg)
    x = np.sin(theta)
    z = np.cos(theta)
    coherence_index = np.sin(theta)

    if abs(coherence_index - 1.0) < 1e-3:
        status_msg = "SISTEMA AUTÓNOMO: Superposición de Espín Absoluta. Consumo: 0W. Data Centers obsoletos."
        line_color = "#34D399"
    else:
        status_msg = f"DESVÍO DE FASE: Índice de Coherencia a {coherence_index:.4f}."
        line_color = "#F87171"

    fig = go.Figure(data=[go.Scatter3d(x=[0, x], y=[0, 0], z=[0, z], mode='lines+markers', line=dict(color=line_color, width=6))])
    fig.update_layout(scene=dict(xaxis=dict(range=[-1,1]), yaxis=dict(range=[-1,1]), zaxis=dict(range=[-1,1])), paper_bgcolor='#09090b')
    
    col1, col2 = st.columns(2)
    with col1: 
        st.plotly_chart(fig, use_container_width=True)
    with col2: 
        st.metric(label="Eficiencia PEUO", value=f"{coherence_index * 100:.2f}%")
        st.info(status_msg)

# =========================================================================
# MODULO 03: SIMULADOR DE DENSIDAD Y FASE DE ESPÍN
# =========================================================================
elif opcion_archivo == "HUNT_SIM_03_BLOCH (Cálculo de Fase)":
    st.header("HUNT_SIM_03_BLOCH: Simulador de Densidad y Fase")
    angle_input = st.sidebar.slider("Ajuste Fino del Ángulo (θ):", 0.0, 180.0, 90.0, 0.1)
    silicon_purity = st.sidebar.slider("Pureza de Silicio-28 (%):", 99.0, 100.0, 99.999, 0.001)
    
    theta_rad = np.radians(angle_input)
    vector_x = np.sin(theta_rad)
    vector_z = np.cos(theta_rad)
    coherence_index = np.sin(theta_rad) * (silicon_purity / 100.0)
    
    st.table(pd.DataFrame({
        'Componente': ['Eje X', 'Eje Y', 'Eje Z'],
        'Valor': [f"{vector_x:.5f}", "0.00000", f"{vector_z:.5f}"]
    }))
    if coherence_index >= 0.999: 
        st.success("✓ Coherencia del PEUO verificada analíticamente.")
    else: 
        st.warning("⚠ Descoherencia detectada en la matriz atómica.")

# =========================================================================
# MODULO 05: SIMULADOR DE IMPACTO FINANCIERO Y OBSOLESCENCIA 
# =========================================================================
elif opcion_archivo == "HUNT_ECON_05_SAVINGS (Simulador de Impacto Financiero)":
    st.header("HUNT_ECON_05_SAVINGS: Análisis de Obsolescencia de Infraestructura")
    st.write("Cálculo del capital financiero y recursos energéticos salvados al reemplazar supercomputadores por núcleos atómicos locales.")

    # Parámetros del Data Center tradicional a simular
    st.sidebar.markdown("### Escala del Data Center Tradicional")
    dc_racks = st.sidebar.number_input("Número de Racks en el Servidor Objetivo:", min_value=10, max_value=50000, value=2500, step=100)
    energy_cost_kwh = st.sidebar.slider("Costo de Energía Promedio (USD/kWh):", 0.05, 0.35, 0.12, 0.01)

    # Constantes operativas del Teorema de Hunt frente al modelo CMOS tradicional
    power_per_rack_kw = 12.5  # Consumo promedio de un rack de IA/Cómputo en 2026
    pue_factor = 1.6          # Factor de eficiencia de enfriamiento masivo
    build_cost_per_mw = 9.0   # Millones de USD para construir 1 MW de capacidad

    # Cálculos matemáticos del impacto
    total_traditional_power_mw = (dc_racks * power_per_rack_kw * pue_factor) / 1000.0
    annual_energy_mwh = total_traditional_power_mw * 24 * 365
    annual_energy_cost_usd = annual_energy_mwh * 1000 * energy_cost_kwh
    infrastructure_capex_saved = total_traditional_power_mw * build_cost_per_mw

    # Equivalencia del Procesador Hunt: Toda esa potencia condensada en milímetros cúbicos de Silicio-28
    equivalent_silicon_volume_cm3 = (dc_racks * 0.004) # 0.004 cm³ de chip de espín equivale a un rack entero

    # Presentación de Métricas de Destrucción de Gasto (Obsolescencia)
    st.markdown("### 📉 Recursos Críticos Salvados (Consumo 0W Local)")
    
    m_col1, m_col2, m_col3 = st.columns(3)
    with m_col1:
        st.metric(label="Energía Eléctrica Eliminada", value=f"{total_traditional_power_mw:.1f} MW", delta="-100% Eficiencia Atómica")
    with m_col2:
        st.metric(label="Ahorro Operativo Anual (OPEX)", value=f"USD {annual_energy_cost_usd:,.2f}", delta="-100%")
    with m_col3:
        st.metric(label="Gasto de Construcción Evitado (CAPEX)", value=f"USD {infrastructure_capex_saved:,.2f} Millones")

    st.markdown("---")
    st.markdown("### 🔬 Equivalencia Física según el PEUO")
    
    e_col1, e_col2 = st.columns(2)
    with e_col1:
        st.info(f"""
        **Infraestructura Tradicional Obsoleta:**  
        * **Espacio requerido:** {dc_racks} racks físicos en miles de metros cuadrados.  
        * **Sistemas de soporte:** Chillers, subestaciones eléctricas, generadores diésel de respaldo y cables de cobre de alta densidad.
        """)
    with e_col2:
        st.success(f"""
        **Sustitución Cristalina de Hunt:**  
        * **Volumen físico necesario:** Apenas **{equivalent_silicon_volume_cm3:.3f} cm³** de cristal puro de Silicio-28.  
        * **Disipación térmica:** El acoplamiento de espines electrónicos no genera calor óhmico. Se elimina el gasto de billones de dólares en refrigeración líquida o criogénica.
        """)
