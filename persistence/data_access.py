"""
CST8002 Programming Language Research Project
Professor: Stanley Pieda
Due Date: 06/15/2025
Author: Rachid Hankir
"""

import csv
import uuid
from model.EmissionRecord import EmissionRecord

# Classe pour gérer l'accès aux données (lecture et écriture CSV)
# Class to manage data access (CSV reading and writing)
class DataAccess:
    """
    A class to handle persistence operations for emission records.
    """
    # Lecture des enregistrements depuis un fichier CSV
    # Read records from a CSV file
    def read_records(self, filename, max_records=100):
        """
        Read emission records from a CSV file.

        Args:
            filename (str): Path to the CSV file.
            max_records (int): Maximum number of records to read (default 100).

        Returns:
            list: List of EmissionRecord objects.

        Raises:
            FileNotFoundError: If the file is not found.
            UnicodeDecodeError: If the file cannot be decoded.
            Exception: For other file reading errors.
        """
        # Initialisation d'une liste vide pour les enregistrements
        # Initialize an empty list for records
        records = []
        # Liste des encodages à essayer
        # List of encodings to try
        encodings = ['utf-8', 'latin-1']
        for encoding in encodings:
            try:
                # Ouverture du fichier en mode lecture
                # Open the file in read mode
                with open(filename, mode='r', encoding=encoding) as file:
                    # Création d'un lecteur CSV
                    # Create a CSV reader
                    csv_reader = csv.reader(file)
                    # Sauter l'en-tête
                    # Skip the header
                    next(csv_reader, None)
                    # Lecture des lignes jusqu'à max_records
                    # Read rows up to max_records
                    for row, _ in zip(csv_reader, range(max_records)):
                        # Compléter les lignes incomplètes
                        # Complete incomplete rows
                        while len(row) < 14:
                            row.append('')
                        # Créer un objet EmissionRecord
                        # Create an EmissionRecord object
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
                        # Ajouter à la liste
                        # Add to the list
                        records.append(record)
                    return records
            except FileNotFoundError:
                # Afficher une erreur si le fichier est manquant
                # Display an error if the file is missing
                print(f"Error: The file '{filename}' was not found.")
                return []
            except UnicodeDecodeError:
                # Passer à l'encodage suivant si échec
                # Try the next encoding if it fails
                if encoding == encodings[-1]:
                    print(f"Error: Unable to decode file '{filename}' with tried encodings.")
                    return []
                continue
            except Exception as e:
                # Afficher toute autre erreur
                # Display any other error
                print(f"Error reading file with {encoding}: {e}")
                return []
        return []

    # Écriture des enregistrements dans un nouveau fichier CSV avec un UUID
    # Write records to a new CSV file with a UUID
    def write_records(self, records):
        """
        Write emission records to a new CSV file with a UUID-generated name.

        Args:
            records (list): List of EmissionRecord objects to write.

        Returns:
            str: Name of the generated CSV file.

        Raises:
            Exception: For file writing errors.
        """
        # Générer un nom de fichier unique avec UUID
        # Generate a unique filename with UUID
        filename = f"output_{uuid.uuid4()}.csv"
        try:
            # Ouverture du fichier en mode écriture
            # Open the file in write mode
            with open(filename, mode='w', encoding='utf-8', newline='') as file:
                # Création d'un écrivain CSV
                # Create a CSV writer
                csv_writer = csv.writer(file)
                # Écrire l'en-tête
                # Write the header
                csv_writer.writerow([
                    "NPRI ID", "Facility name", "Company name", "Address", "City",
                    "Province", "PostalCode", "Latitude", "Longitude", "Emissions",
                    "Units", "Facility details", "Facility information", "Report year"
                ])
                # Écrire chaque enregistrement
                # Write each record
                for record in records:
                    csv_writer.writerow([
                        record.npri_id, record.facility_name, record.company_name,
                        record.address, record.city, record.province, record.postal_code,
                        record.latitude, record.longitude, record.emissions, record.units,
                        record.facility_details, record.facility_information, record.report_year
                    ])
            # Retourner le nom du fichier généré
            # Return the generated filename
            return filename
        except Exception as e:
            # Afficher une erreur en cas d'échec d'écriture
            # Display an error if writing fails
            print(f"Error writing to file {filename}: {e}")
            return None