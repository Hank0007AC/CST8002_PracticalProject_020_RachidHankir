"""
CST8002 Programming Language Research Project
Practical Project Part 04
Professor: Stanley Pieda
Due Date: 07/29/2025
Author: Rachid Hankir
"""

from persistence.data_access import DataAccess
from model.BasicEmissionRecord import BasicEmissionRecord  # Importer la sous-classe par défaut pour chargement
from model.DetailedEmissionRecord import DetailedEmissionRecord  # Importer pour création détaillée

# Classe pour gérer la logique métier des enregistrements d'émissions
# Class to manage the business logic of emission records
class EmissionManager:
    """
    A class to manage emission records, including CRUD operations and data persistence.
    Updated for Practical Project Part 3 to support polymorphism with Record subclasses and format selection.
    Updated for Practical Project Part 4 to support multi-column filtering.
    """
    # Initialisation avec une instance de DataAccess
    # Initialization with a DataAccess instance
    def __init__(self):
        """
        Initialize the EmissionManager with an empty record list and DataAccess.
        """
        # Liste pour stocker les enregistrements en mémoire (type Record pour polymorphisme)
        # List to store records in memory (Record type for polymorphism)
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

    # Afficher un ou plusieurs enregistrements avec option de format
    # Display one or multiple records with format option
    def display_records(self, index=None, format_type='basic'):
        """
        Display records using specified format type.

        Args:
            index (int, optional): Index of the record to display. Defaults to None (all records).
            format_type (str): 'basic' or 'detailed' to force format (default 'basic').

        Returns:
            list: List of displayed records.
        """
        # Liste des enregistrements à afficher
        # List of records to display
        display_list = [self._records[index]] if index is not None else self._records
        for i, record in enumerate(display_list):
            if format_type == 'detailed':
                # Affichage détaillé avec plus de champs : année | nom installation | nom entreprise | ville | province | adresse | latitude | longitude | émissions | unités | détails installation
                # Detailed display with more fields: year | facility_name | company_name | city | province | address | latitude | longitude | emissions | units | facility_details
                print(f"Record {i + 1}: {record.report_year} | {record.facility_name} | {record.company_name} | {record.city} | {record.province} | {record.address} | {record.latitude} | {record.longitude} | {record.emissions} {record.units} | {record.facility_details}")
            else:
                # Affichage basique : année | nom installation | émissions unités
                # Basic display: year | facility_name | emissions units
                print(f"Record {i + 1}: {record.report_year} | {record.facility_name} | {record.emissions} {record.units}")
        return display_list

    # Créer un nouvel enregistrement (par défaut BasicEmissionRecord)
    # Create a new record (default BasicEmissionRecord)
    def create_record(self, npri_id, facility_name, company_name, address, city, province, postal_code, latitude, longitude, emissions, units, facility_details, facility_information, report_year, format_type='basic'):
        """
        Create and add a new emission record using subclass based on format_type.

        Args:
            ... (inherited)
            format_type (str): 'basic' for BasicEmissionRecord or 'detailed' for DetailedEmissionRecord.

        Returns:
            Record: The created record.
        """
        # Choisir la sous-classe en fonction du type de format
        # Choose the subclass based on the format type
        if format_type == 'detailed':
            record = DetailedEmissionRecord(
                npri_id, facility_name, company_name, address, city, province,
                postal_code, latitude, longitude, emissions, units, facility_details,
                facility_information, report_year
            )
        else:
            record = BasicEmissionRecord(
                npri_id, facility_name, company_name, address, city, province,
                postal_code, latitude, longitude, emissions, units, facility_details,
                facility_information, report_year
            )
        # Ajouter à la liste
        # Add to the list
        self._records.append(record)
        return record

    # Modifier un enregistrement existant (compatible avec polymorphisme)
    # Edit an existing record (compatible with polymorphism)
    def edit_record(self, index, npri_id=None, facility_name=None, company_name=None, address=None, city=None, province=None, postal_code=None, latitude=None, longitude=None, emissions=None, units=None, facility_details=None, facility_information=None, report_year=None):
        """
        Edit an existing emission record by index.

        Args:
            index (int): Index of the record to edit.
            ... (inherited)

        Returns:
            bool: True if successful, False if index invalid.
        """
        # Vérifier si l'index est valide
        # Check if the index is valid
        if 0 <= index < len(self._records):
            record = self._records[index]
            # Mettre à jour les champs non nuls via setters (hérités de Record)
            # Update non-null fields via setters (inherited from Record)
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

    # Supprimer un enregistrement (compatible avec polymorphisme)
    # Delete a record (compatible with polymorphism)
    def delete_record(self, index):
        """
        Delete a record by index.

        Args:
            index (int): Index of the record to edit.
            ... (inherited)

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
            list: List of Record objects.
        """
        return self._records

    # Nouvelle méthode pour filtrer les enregistrements sur plusieurs colonnes (Part 4)
    # New method to filter records on multiple columns (Part 4)
    def filter_records(self, city=None, emissions_min=None):
        """
        Filter records based on city and minimum emissions value.

        Args:
            city (str, optional): City to filter by.
            emissions_min (float, optional): Minimum emissions value to filter by.

        Returns:
            list: Filtered list of Record objects.
        """
        # Filtrer la liste des enregistrements selon les critères fournis
        # Filter the list of records based on the provided criteria
        filtered = self._records
        if city is not None:
            # Filtrer par ville (insensible à la casse)
            # Filter by city (case-insensitive)
            filtered = [r for r in filtered if r.city.lower() == city.lower()]
        if emissions_min is not None:
            # Filtrer par émissions minimales
            # Filter by minimum emissions
            filtered = [r for r in filtered if r.emissions >= emissions_min]
        # Retourner la liste filtrée
        # Return the filtered list
        return filtered