import requests

URL_FUENTE = "http://mmarc.ar"
ARCHIVO_SALIDA = "lista.m3u"

def generar_lista():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': '*/*'
    }
    
    try:
        print("Descargando canales desde mmarc.ar...")
        response = requests.get(URL_FUENTE, headers=headers, timeout=20)
        
        if response.status_code == 200:
            contenido = response.text
            
            # Guardamos el archivo directamente
            with open(ARCHIVO_SALIDA, "w", encoding="utf-8") as f:
                f.write(contenido)
            print(f"¡Éxito! Archivo {ARCHIVO_SALIDA} actualizado.")
        else:
            print(f"Error de conexión. Código: {response.status_code}")
            
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    generar_lista()
