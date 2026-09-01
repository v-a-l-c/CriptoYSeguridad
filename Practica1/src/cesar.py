import sys
import os

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
    "PDF":  bytes([0x25, 0x50, 0x44, 0x46]),
    "EPUB": bytes([0x50, 0x4B, 0x03, 0x04])
}

def decrypt_file(filepath: str, k: int, ext: str):
    """Lee todo el archivo cifrado, aplica el corrimiento inverso (b - k) % 256 y guarda el resultado."""
    base_name = os.path.splitext(filepath)[0]
    output_filepath = f"{base_name}_descifrado.{ext.lower()}" # Dirección del archivo
    
    with open(filepath, "rb") as f_in: # Lee en binario
        content = f_in.read()

    decrypted_content = bytes((b - k) % 256 for b in content)

    with open(output_filepath, "wb") as f_out:
        f_out.write(decrypted_content)

    print(f"[+] Archivo descifrado guardado como: {output_filepath}")

def analyze_bytes(filepath: str, n: int = 256):
    """
    
    """
    try:
        with open(filepath, "rb") as file: # Lee el archivo en binario
            header = file.read(8) # Lee los primeros 8 bytes
            
        if not header:
            print("El archivo está vacío.")
            return

        coincidencias = []

        # Se prueba con K en [1 .. 255]
        for k in range(1, n):
            decrypted_header = bytes((b - k) % 256 for b in header)

            is_mp4 = decrypted_header[4:8] == magic_bytes["MP4"]

            for fmt, magic in magic_bytes.items():
                if fmt == "MP4" and is_mp4:
                    coincidencias.append((k, fmt, decrypted_header))
                elif fmt != "MP4" and decrypted_header.startswith(magic):
                    coincidencias.append((k, fmt, decrypted_header))

        if coincidencias:
            print("Clave encontrada")
            for k, fmt, dec_bytes in coincidencias:
                hex_preview = " ".join(f"{b:02X}" for b in dec_bytes)
                print(f"[+] Clave (k): {k} | Formato: {fmt}")
                print(f"    Bytes descifrados: {hex_preview}")
                
                decrypt_file(filepath, k, fmt)
        else:
            print("No se encontraron coincidencias con la lista de magic bytes.")

    except FileNotFoundError:
        print(f"Error: El archivo '{filepath}' no existe.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")

def main(filepath: str):
    analyze_bytes(filepath)

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        main(sys.argv[1])
    else:
        print("Por favor ingrese la dirección del archivo")
