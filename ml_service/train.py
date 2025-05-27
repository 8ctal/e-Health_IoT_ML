import joblib
from sklearn.linear_model import LogisticRegression
import numpy as np

# Datos de entrenamiento más realistas
X = np.array([
    # Casos normales
    [70, 120, 80],  # Normal
    [75, 118, 78],  # Normal
    [68, 122, 75],  # Normal
    [72, 125, 82],  # Normal
    [65, 115, 70],  # Normal
    [80, 130, 85],  # Normal
    [85, 135, 88],  # Normal
    [90, 140, 90],  # Normal
    
    # Casos anormales
    [110, 160, 100],  # Taquicardia + Hipertensión severa
    [45, 90, 60],     # Bradicardia + Hipotensión
    [120, 180, 110],  # Taquicardia severa + Hipertensión severa
    [130, 190, 120],  # Taquicardia severa + Hipertensión severa
    [40, 85, 55],     # Bradicardia severa + Hipotensión
    [100, 150, 95],   # Taquicardia + Hipertensión
    [95, 145, 90],    # Taquicardia + Hipertensión
    [50, 95, 65]      # Bradicardia + Hipotensión
])

# 0 = normal, 1 = anormal
y = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]

model = LogisticRegression()
model.fit(X, y)
joblib.dump(model, "model.pkl")