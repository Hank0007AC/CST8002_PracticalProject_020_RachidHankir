"""
CST8002 Programming Language Research Project
Practical Project Part 02
Professor: Stanley Pieda
Due Date: 06/15/2025
Author: Rachid Hankir
"""

from persistence.data_access import DataAccess
from model.EmissionRecord import EmissionRecord

# Classe pour gérer la logique métier des enregistrements d'émissions
# Class to manage the business logic of emission records
class EmissionManager:
    """
    A class to manage emission records, including CRUD operations and data persistence.
    """
    # Initialisation avec une instance de DataAccess
    # Initialization with a DataAccess instance
    def __init__(self):
        """
        Initialize the EmissionManager with an empty record list and DataAccess.
        """
        # Liste pour stocker les enregistrements en mémoire
        # List to store records in memory
        self._records = []
        # Instance de DataAccess pour les opérations de persistance
        # DataAccess instance for persistence operations
        self._data_access = DataAccess()

    # Recharger les données depuis le CSV
    # Reload data from the CSV
    def reload_data(self, filename):
        """
        Reload records from the specified CSV file.

        Args:
            filename (str): Path to the CSV file.

        Returns:
            bool: True if successful, False otherwise.
        """
        # Lire les enregistrements via la couche de persistance
        # Read records via the persistence layer
        self._records = self._data_access.read_records(filename)
        # Retourner si la lecture a réussi
        # Return whether the read was successful
        return len(self._records) > 0

    # Sauvegarder les données dans un nouveau CSV
    # Save data to a new CSV
    def save_data(self):
        """
        Save current records to a new CSV file with a UUID name.

        Returns:
            str: Name of the generated file, or None if failed.
        """
        # Sauvegarder via la couche de persistance
        # Save via the persistence layer
        return self._data_access.write_records(self._records)

    # Afficher un ou plusieurs enregistrements
    # Display one or multiple records
    def display_records(self, index=None):
        """
        Display records, either all or a specific one.

        Args:
            index (int, optional): Index of the record to display. Defaults to None (all records).

        Returns:
            list: List of displayed records.
        """
        # Liste enregistrement à afficher
        # List of records to display
        display_list = [self._records[index]] if index is not None else self._records
        # Afficher chaque enregistrement
        # Display each record
        for i, record in enumerate(display_list):
            print(f"Record {i + 1}: {record}")
        return display_list

    # Créer un nouvel enregistrement
    # Create a new record
    def create_record(self, npri_id, facility_name, company_name, address, city, province, postal_code, latitude, longitude, emissions, units, facility_details, facility_information, report_year):
        """
        Create and add a new emission record.

        Args:
            npri_id (str): The NPRI ID.
            facility_name (str): The facility name.
            company_name (str): The company name.
            address (str): The address.
            city (str): The city.
            province (str): The province.
            postal_code (str): The postal code.
            latitude (float): The latitude.
            longitude (float): The longitude.
            emissions (float): The emission value.
            units (str): The units of measurement.
            facility_details (str): Facility details.
            facility_information (str): Facility information.
            report_year (int): The report year.

        Returns:
            EmissionRecord: The created record.
        """
        # Créer un nouvel objet EmissionRecord
        # Create a new EmissionRecord object
        record = EmissionRecord(
            npri_id, facility_name, company_name, address, city, province,
            postal_code, latitude, longitude, emissions, units, facility_details,
            facility_information, report_year
        )
        # Ajouter à la liste
        # Add to the list
        self._records.append(record)
        return record

    # Modifier un enregistrement existant
    # Edit an existing record
    def edit_record(self, index, npri_id=None, facility_name=None, company_name=None, address=None, city=None, province=None, postal_code=None, latitude=None, longitude=None, emissions=None, units=None, facility_details=None, facility_information=None, report_year=None):
        """
        Edit an existing emission record by index.

        Args:
            index (int): Index of the record to edit.
            npri_id (str, optional): New NPRI ID.
            facility_name (str, optional): New facility name.
            ... (other optional fields)
            report_year (int, optional): New report year.

        Returns:
            bool: True if successful, False if index invalid.
        """
        # Vérifier si l'index est valide
        # Check if the index is valid
        if 0 <= index < len(self._records):
            record = self._records[index]
            # Mettre à jour les champs non nuls
            # Update non-null fields
            if npri_id is not None:
                record.npri_id = npri_id
            if facility_name is not None:
                record.facility_name = facility_name
            if company_name is not None:
                record.company_name = company_name
            if address is not None:
                record.address = address
            if city is not None:
                record.city = city
            if province is not None:
                record.province = province
            if postal_code is not None:
                record.postal_code = postal_code
            if latitude is not None:
                record.latitude = latitude
            if longitude is not None:
                record.longitude = longitude
            if emissions is not None:
                record.emissions = emissions
            if units is not None:
                record.units = units
            if facility_details is not None:
                record.facility_details = facility_details
            if facility_information is not None:
                record.facility_information = facility_information
            if report_year is not None:
                record.report_year = report_year
            return True
        return False

    # Supprimer un enregistrement
    # Delete a record
    def delete_record(self, index):
        """
        Delete a record by index.

        Args:
            index (int): Index of the record to delete.

        Returns:
            bool: True if successful, False if index invalid.
        """
        # Vérifier si l'index est valide
        # Check if the index is valid
        if 0 <= index < len(self._records):
            # Supprimer l'enregistrement
            # Delete the record
            self._records.pop(index)
            return True
        return False

    # Obtenir la liste des enregistrements
    # Get the list of records
    def get_records(self):
        """
        Get the current list of records.

        Returns:
            list: List of EmissionRecord objects.
        """
        return self._records