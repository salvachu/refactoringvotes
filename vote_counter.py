import csv

def count_votes(file_path):
    """
    Cuenta los votos para cada candidato a partir de un archivo CSV y muestra los resultados.
    
    input:
    - file_path (str): Ruta al archivo CSV que contiene los votos.
    
    output:
    - str: Nombre del candidato con la mayor cantidad de votos.
    """
    results = {}

    # Usar 'with' asegura que el archivo se cierre correctamente después de leerlo
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)  # Omitir el encabezado

        # Recorrer cada fila en el archivo CSV para contar los votos
        for row in reader:
            city = row[0]
            candidate = row[1]
            
            # Intentar convertir los votos a entero y asignar 0 en caso de error
            try:
                votes = int(row[2])
            except ValueError:
                votes = 0  # Asignar 0 para conteos de votos no válidos o faltantes
            
            # Actualización simplificada del diccionario usando el método 'get' con valor por defecto
            results[candidate] = results.get(candidate, 0) + votes

    # Mostrar el total de votos por candidato
    for candidate, total_votes in results.items():
        print(f"{candidate}: {total_votes} votos")

    # Ordenar los candidatos por votos en orden descendente y declarar al ganador
    sorted_by_votes = sorted(results.items(), key=lambda item: item[1], reverse=True)
    winner = sorted_by_votes[0][0]
    print(f"El ganador es {winner}")
    
    return winner  # Devolver el ganador para su uso potencial en pruebas

# Ejemplo de uso
count_votes('votes.csv')
