import json
import csv

# Lire le fichier JSON
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

# Ouvrir un fichier CSV en écriture
with open('output.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Écrire l'en-tête du fichier CSV
    csv_writer.writerow(['reel', 'imaginaire'])
    # Écrire chaque nombre complexe dans le fichier CSV
    for complex_number in data:
        csv_writer.writerow(complex_number)

print("Les nombres complexes ont été écrits dans output.csv")
