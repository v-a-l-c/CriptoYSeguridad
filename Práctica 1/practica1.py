# Practiza 1


def base64(texto_b64):
    # Definimos el alfabeto
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    
    padding = texto_b64.count('=')
    texto_b64 = texto_b64.rstrip('=') #Para limpiar el padding

    bits = ""
    for caracter in texto_b64:
        if caracter in alfabeto:
            valor_entero = alfabeto.index(caracter)
            # Convertimos a binario y se rellena con ceros a la izquierda hasta tener 6 bits
            bits += f"{valor_entero:06b}"
            
    # Agrupamos los bits en bloques
    bytes_resultado = []
    for i in range(0, len(bits), 8):
        bloque_8 = bits[i:i+8]
        if len(bloque_8) == 8:
            bytes_resultado.append(int(bloque_8, 2))
        print("descifradito")

    return bytes(bytes_resultado)