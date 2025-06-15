"""
CST8002 Programming Language Research Project
Practical Project Part 02
Professor: Stanley Pieda
Due Date: 06/15/2025
Author: Rachid Hankir
"""

# Importation du module csv pour lire le fichier CSV
import csv
# Importation de la classe EmissionRecord depuis EmissionRecord.py
from EmissionRecord import EmissionRecord

# Fonction pour lire les données du CSV et créer des objets EmissionRecord
def read_emission_data(filename, max_records=5):
    """
    Read the emission dataset from a CSV file and return a list of EmissionRecord objects.

    Args:
        filename (str): The path to the CSV file.
        max_records (int): Maximum number of records to read (default is 5).

    Returns:
        list: A list of EmissionRecord objects.

    Raises:
        FileNotFoundError: If the CSV file is not found.
        UnicodeDecodeError: If the file cannot be decoded with the tried encodings.
        Exception: For other errors during file reading or parsing.
    """
    # Initialisation d'une liste vide pour stocker les objets EmissionRecord
    records = []
    # Liste des encodages à essayer pour lire le fichier
    encodings = ['utf-8', 'latin-1']
    # Boucle pour essayer chaque encodage
    for encoding in encodings:
        # Bloc try pour gérer les exceptions
        try:
            # Ouverture du fichier CSV en mode lecture avec l'encodage actuel
            with open(filename, mode='r', encoding=encoding) as file:
                # Création d'un lecteur CSV pour parcourir les lignes
                csv_reader = csv.reader(file)
                # Sauter la première ligne (en-tête)
                next(csv_reader, None)
                # Boucle pour lire jusqu'à max_records lignes
                for row, _ in zip(csv_reader, range(max_records)):
                    # Ajouter des chaînes vides si la ligne a moins de 14 colonnes
                    while len(row) < 14:
                        row.append('')
                    # Création d'un objet EmissionRecord avec les données de la ligne
                    record = EmissionRecord(
                        npri_id=row[0],
                        facility_name=row[1],
                        company_name=row[2],
                        address=row[3],
                        city=row[4],
                        province=row[5],
                        postal_code=row[6],
                        latitude=row[7],
                        longitude=row[8],
                        emissions=row[9],
                        units=row[10],
                        facility_details=row[11],
                        facility_information=row[12],
                        report_year=row[13]
                    )
                    # Ajout de l'objet à la liste
                    records.append(record)
                # Retourner la liste des enregistrements
                return records
        # Gestion de l'erreur si le fichier n'existe pas
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
            return []
        # Gestion de l'erreur d'encodage
        except UnicodeDecodeError:
            if encoding == encodings[-1]:
                print(f"Error: Unable to decode file '{filename}' with tried encodings.")
                return []
            continue
        # Gestion des autres erreurs
        except Exception as e:
            print(f"Error reading file with {encoding}: {e}")
            return []
    # Retourner une liste vide si tous les encodages échouent
    return []

# Fonction pour afficher les enregistrements
def display_records(records):
    """
    Display all records in the provided list.

    Args:
        records (list): List of EmissionRecord objects to display.
    """
    # Vérifier si la liste est vide
    if not records:
        print("No records to display.")
        return
    # Afficher le nombre d'enregistrements chargés
    print(f"Loaded {len(records)} records.\n")
    # Boucle pour afficher chaque enregistrement
    for record in records:
        # Appel de la méthode __str__ de l'objet EmissionRecord
        print(record)

# Fonction principale du programme
def main():
    """
    Main function to run the program, displaying the student's name and emission records.
    """
    # Définition du nom complet
    full_name = "Rachid Hankir"
    # Affichage du nom au début
    print(f"\nAuthor: {full_name}\n")
    
    # Nom du fichier CSV
    filename = "Nitrogen oxide emissions by facility.csv"
    # Lecture des enregistrements en appelant read_emission_data
    emission_records = read_emission_data(filename)
    
    # Affichage des en-têtes pour les enregistrements
    print("Emission Records:")
    # Affichage des enregistrements en appelant display_records
    display_records(emission_records)
    
    # Affichage du nom à la fin
    print(f"\nProgram completed. \nPrepared by: {full_name}\n")
    # Pause pour garder l'output visible
    input("Press Enter to exit...")

# Exécution du programme si le fichier est lancé directement
if __name__ == "__main__":
    main()