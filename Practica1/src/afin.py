# Diccionario enfocado estrictamente en documentos, imágenes y videos
magic_bytes = {
    # Imagen
    "PNG": bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]),
    "JPG": bytes([0xFF, 0xD8, 0xFF]),
    "BMP": bytes([0x42, 0x4D]),

    # Audio
    "MP3": bytes([0x49, 0x44, 0x33]),
    "WAV": bytes([0x52, 0x49, 0x46, 0x46]),
    "OGG": bytes([0x4F, 0x67, 0x67, 0x53]),

    # Video
    "MP4": bytes([0x66, 0x74, 0x79, 0x70]),
    "AVI": bytes([0x52, 0x49, 0x46, 0x46]),
    "MKV": bytes([0x1A, 0x45, 0xDF, 0xA3]),

    # Documento
    "DOCX": bytes([0x50, 0x4B, 0x03, 0x04]),
    "PDF": bytes([0x25, 0x50, 0x44, 0x46]),
    "EPUB": bytes([0x50, 0x4B, 0x03, 0x04])
}

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def buscar_claves_reales(ruta_archivo):
    with open(ruta_archivo, 'rb') as f:
        # Leemos 32 bytes para tener más contexto
        cabecera = f.read(32)

    coincidencias = []

    for a in range(1, 256, 2):  
        a_inv = mod_inverse(a, 256)
        if not a_inv: continue
        
        for b in range(256):
            decrypted_chunk = bytearray(
                (a_inv * (byte - b)) % 256 for byte in cabecera
            )
            
            # Comprobar contra firmas seguras
            for ext, magic in magic_bytes.items():
                if decrypted_chunk.startswith(magic):
                    coincidencias.append((a, b, ext))
                    
    if coincidencias:

        a, b, ext = coincidencias[0]

        import os
        base_name = os.path.splitext(ruta_archivo)[0]
        output_filepath = f"{base_name}.{ext.lower()}" # Dirección del archivo
        
        # Descifrar el archivo
        print(f"\nDescifrando con claves: a={a}, b={b}...")
        descifrar_archivo(ruta_archivo, output_filepath, a, b)


def descifrar_archivo(ruta_entrada, ruta_salida, a, b):
    """Descifra un archivo cifrado con cifrado afín usando las claves a y b"""
    a_inv = mod_inverse(a, 256)
    if not a_inv:
        print(f"Error: {a} no tiene inverso módulo 256")
        return False
    
    try:
        with open(ruta_entrada, 'rb') as f_entrada:
            datos_cifrados = f_entrada.read()
        
        # Descifrar byte por byte
        datos_descifrados = bytearray()
        for byte in datos_cifrados:
            # Fórmula de descifrado afín: P = a_inv * (C - b) mod 256
            byte_descifrado = (a_inv * (byte - b)) % 256
            datos_descifrados.append(byte_descifrado)
        
        # Escribir el archivo descifrado
        with open(ruta_salida, "wb") as salida:  # <- Usar ruta_salida, no sobreescribir
            salida.write(datos_descifrados)

        return True
        
    except Exception as e:
        print(f"Error al descifrar: {e}")
        return False
