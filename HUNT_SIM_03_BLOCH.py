# Simulador matemático de la estabilidad del espín
import numpy as np

def calculate_spin_vector(theta_deg):
    theta = np.radians(theta_deg)
    x = np.sin(theta)
    y = 0.0
    z = np.cos(theta)
    coherence_index = np.sin(theta)
    return {"vector": (x, y, z), "coherence": coherence_index}

if __name__ == "__main__":
    result = calculate_spin_vector(90)
    print(f"[PEUO SIM] Coherencia al ángulo óptimo: {result['coherence'] * 100}%")
