# Mi Proyecto de Python

Este es un proyecto en Python que utiliza un entorno virtual para gestionar las dependencias, y está diseñado para demostrar **cómo una red neuronal produce predicciones en un modelo de regresión lineal**. La versión de Python utilizada es **3.10.11**.

## Estructura del Proyecto

El proyecto tiene la siguiente estructura:

```
RedNeuronal/
│
├── .gitignore               # Archivos y carpetas que Git debe ignorar
├── README.md                # Este archivo de documentación
├── requirements.txt         # Archivo con las dependencias del proyecto
│
├── venv/                    # Entorno virtual (será ignorado por Git)
│
└── src/                     # Código fuente del proyecto
    └── main.py              # Script principal donde se ejecuta el código
```

- **`.gitignore`**: Lista de archivos y carpetas que Git no debe rastrear, como el entorno virtual y archivos generados automáticamente.
- **`README.md`**: Documentación del proyecto, incluyendo una descripción general y cómo ejecutar el proyecto.
- **`requirements.txt`**: Contiene las dependencias necesarias para el proyecto. Para instalar todas las dependencias, ejecuta `pip install -r requirements.txt`.
- **`venv/`**: El entorno virtual donde se instalan las dependencias del proyecto. Este directorio no se sube a GitHub gracias al archivo `.gitignore`.
- **`src/`**: Carpeta que contiene el código fuente del proyecto. Actualmente, el archivo principal es `main.py`, donde se ejecuta el flujo principal del programa.

## Requisitos

- Python 3.10.11
- Dependencias (instalar con `pip install -r requirements.txt`)

## Instalación

1. Clona el repositorio:
   ```
   git clone https://github.com/andlopezval/RedNeuronal01.git
   ```
2. Crea un entorno virtual:
   ```
   python -m venv venv
   ```
3. Activa el entorno virtual:
   - En **Windows**:
     ```
     .\venv\Scripts\activate
     ```
   - En **macOS/Linux**:
     ```
     source venv/bin/activate
     ```
4. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Uso

Para ejecutar el proyecto, simplemente corre el siguiente comando:

```
python src/main.py
```

