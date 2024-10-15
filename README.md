
# Multi Web Viewer con PyQt5

Este proyecto es una aplicación de Python que permite visualizar múltiples sitios web simultáneamente en una ventana sin bordes y en pantalla completa, utilizando `PyQt5` y `PyQtWebEngine`. La interfaz se ajusta automáticamente en función del número de URLs proporcionadas.

## Requisitos

### Requerimientos del Sistema
- **Sistema Operativo**: Windows 10/11
- **Python**: 3.8 o superior
- -**Visual C++**: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/

### Instalación de Dependencias

1. Asegúrate de tener **pip** actualizado:
   ```bash
   python -m pip install --upgrade pip
   ```

2. Instala las dependencias desde el archivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

3. Si tienes problemas con la instalación, puede ser necesario instalar **Microsoft Visual C++ Build Tools** desde [este enlace](https://visualstudio.microsoft.com/visual-cpp-build-tools/). Asegúrate de seleccionar las opciones:
   - **Desarrollo para escritorio con C++**
   - **MSVC v143 - VS 2022 C++ x64/x86 build tools**
   - **Windows 10 SDK**

### Ejecución del Script

1. Guarda el código en un archivo llamado `multi_web_viewer.py`.
2. Asegúrate de que las dependencias estén instaladas.
3. Ejecuta el script desde la terminal o línea de comandos con:
   ```bash
   python multi_web_viewer.py
   ```

4. La ventana se abrirá automáticamente en **modo pantalla completa** sin bordes ni barra de título.

### Salida del Modo Pantalla Completa

- Para salir del modo pantalla completa, presiona la tecla **Alt + F4** o utiliza un método adicional implementado en el código (como una combinación de teclas).

### Contribuciones

Si deseas contribuir a este proyecto, siéntete libre de enviar un **pull request** o abrir un **issue** en el repositorio.

### Licencia

Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

### Créditos

Por: D Palacios ® - 2024
