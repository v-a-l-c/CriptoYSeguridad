import sys
import os
from cesar import decrypt_file as cesar_analyze
from afin import buscar_claves_reales as afin_analyze
from decimado import analyze_bytes as decimado_analyze
from base64 import analyze_base64 as base64_analyze

def menu():
    print("\n" + "="*50)
    print("   ANALIZADOR DE ARCHIVOS CIFRADOS")
    print("="*50)
    print("1. Cifrado César")
    print("2. Cifrado Decimado")
    print("3. Cifrado Afín")
    print("4. Codificación Base64")
    print("5. Salir")
    print("="*50)

def main():
    if len(sys.argv) >= 2:
        archivo = sys.argv[1]
    else:
        archivo = input("Ingresa la ruta del archivo cifrado: ")
    
    # Verificar que el archivo existe
    if not os.path.exists(archivo):
        print(f"Error: El archivo '{archivo}' no existe.")
        return
    
    while True:
        menu()
        opcion = input("\nSelecciona una opción (1-5): ")
        
        if opcion == "1":
            print(f"\nAnalizando '{archivo}' con cifrado César...")
            cesar_analyze(archivo)
            
        elif opcion == "2":
            print(f"\nAnalizando '{archivo}' con cifrado Decimado...")
            decimado_analyze(archivo)
            
        elif opcion == "3":
            print(f"\nAnalizando '{archivo}' con cifrado Afín...")
            afin_analyze(archivo)

        elif opcion == "4":
            print(f"\nAnalizando '{archivo}' con codificación Base64...")
            base64_analyze(archivo)

        elif opcion == "5":
            break
            
        else:
            print("Opción inválida. Por favor, selecciona 1-5.")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()