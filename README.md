# HistorialSearch
HistorialSearch es una herramienta de Python para buscar y descargar capturas de pantalla históricas de sitios web utilizando la API de Wayback Machine.
Características

Buscar capturas de pantalla de un sitio web de hace un número específico de años.
Descargar y guardar capturas de pantalla.
Buscar capturas de pantalla por extensiones de archivo específicas.

# Requisitos

Python 3.6+
waybackpy
requests

Instalación

Clona este repositorio:
Copygit clone  
```bash  https://github.com/tuusuario/HistorialSearch.git ```

Navega al directorio del proyecto:
Copycd HistorialSearch

Instala las dependencias:
Copypip install -r requirements.txt


Uso
Aquí hay un ejemplo de cómo usar HistorialSearch:
pythonCopyfrom historial_search import HistorialSearch

# Crear una instancia de HistorialSearch
historial = HistorialSearch("https://example.com", "MyUserAgent/1.0")

# Buscar una captura de pantalla de hace 2 años
historial.search_snapshot()

# Buscar capturas de pantalla por extensiones de archivo
historial.search_snapshots_by_extensions()
Contribuir
Las contribuciones son bienvenidas. Por favor, abre un issue para discutir los cambios propuestos antes de enviar un pull request.
# Licencia
Apache License 2.0