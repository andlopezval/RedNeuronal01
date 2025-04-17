import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import random
from sklearn.model_selection import train_test_split

# Fijar la semilla para reproducibilidad
np.random.seed(42)
tf.random.set_seed(42)
random.seed(42)

# Generar los datos
X = np.linspace(0, 1, 100)  # 100 muestras entre 0 y 1
y = 2 * X + 1 + 0.1 * np.random.randn(100)  # Ecuación lineal + ruido

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo de red neuronal
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(1,)),  # Capa de entrada
    tf.keras.layers.Dense(32, activation='relu'),  # Capa oculta con 32 neuronas y activación ReLU
    tf.keras.layers.Dense(1)  # Capa de salida con una neurona
])

# Compilar el modelo
model.compile(optimizer='adam', loss='mean_squared_error')

# Entrenar el modelo
model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_test, y_test))

# Evaluar el modelo en el conjunto de prueba
test_loss = model.evaluate(X_test, y_test)
print(f"Test Loss: {test_loss:.4f}")

# Realizar predicciones
predictions = model.predict(X_test)

# Graficar los resultados
plt.figure(figsize=(10,6))
plt.scatter(X_test, y_test, color='blue', label='Datos Reales', alpha=0.6)  # Nube de puntos reales
plt.scatter(X_test, predictions, color='red', label='Predicciones', alpha=0.6)  # Nube de puntos predichos
plt.title("Regresión con Red Neuronal")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()

