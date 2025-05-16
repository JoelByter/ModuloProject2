import argparse
import os

# Configurar argumentos
parser = argparse.ArgumentParser(description="Procesa un archivo de datos numéricos.")
parser.add_argument("input_file", help="Ruta al archivo de datos de entrada")
args = parser.parse_args()

# Función para leer datos del archivo
def read_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    datos = []
    for linea in lines:
        linea = linea.strip()
        try:
            datos.append(float(linea))
        except ValueError:
            # Ignorar líneas que no son números válidos
            continue
    return datos

# Función para calcular el promedio
def calculate_average(data):
    return sum(data) / len(data)

# Función para calcular el valor máximo
def calculate_maximum(data):
    return max(data)

# Función para escribir los resultados a un archivo
def write_output(data, average, maximum, output_file='output.txt'):
    with open(output_file, 'w') as file:
        file.write(f"Se procesaron {len(data)} entradas\n")
        file.write(f"Promedio: {average:.2f}\n")
        file.write(f"Máximo: {maximum:.2f}\n")

# Bloque principal de ejecución
if __name__ == "__main__":
    try:
        # Leer y procesar datos
        datos = read_data(args.input_file)
        if not datos:
            raise ValueError("No se encontraron datos válidos.")
        promedio = calculate_average(datos)
        maximo = calculate_maximum(datos)
        write_output(datos, promedio, maximo)
        print("Procesamiento completo. Resultados guardados en 'output.txt'.")
    except Exception as e:
        print(f"Error: {e}")
