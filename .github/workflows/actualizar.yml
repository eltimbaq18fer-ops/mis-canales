name: Actualizar Lista M3U

on:
  schedule:
    - cron: '0 3 * * *' # Se ejecuta automáticamente todos los días a las 3:00 AM UTC
  workflow_dispatch: # Te permite ejecutarlo manualmente cuando quieras

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write # Permiso crucial para que el bot pueda guardar el archivo generado
    steps:
    - uses: actions/checkout@v4
    
    - name: Configurar Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'
        
    - name: Instalar dependencias
      run: pip install -r requirements.txt

    - name: Ejecutar Script
      run: python actualizar.py

    - name: Guardar cambios en el repositorio
      run: |
        git config --global user.name 'github-actions[bot]'
        git config --global user.email 'github-actions[bot]@://github.com'
        git add lista.m3u || true
        git commit -m "Lista actualizada automáticamente" || true
        git push || true
