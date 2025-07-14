"""
CST8002 Programming Language Research Project
Practical Project Part 03
Professor: Stanley Pieda
Due Date: 07/08/2025
Author: Rachid Hankir
"""

from model.Record import Record

# Sous-classe pour un format de sortie basique des enregistrements
# Sub-class for a basic output format of records
class BasicEmissionRecord(Record):
    """
    Sub-class of Record for basic formatted emission records.
    """
    # Constructeur pour initialiser un BasicEmissionRecord, appelant le super
    # Constructor to initialize a BasicEmissionRecord, calling the super
    def __init__(self, npri_id, facility_name, company_name, address, city, province, postal_code, latitude, longitude, emissions, units, facility_details, facility_information, report_year):
        """
        Initialize a BasicEmissionRecord with data from the dataset.

        Args:
            (Inherited from Record)
        """
        # Appel au constructeur de la super-classe Record
        # Call to the super-class Record constructor
        super().__init__(npri_id, facility_name, company_name, address, city, province, postal_code, latitude, longitude, emissions, units, facility_details, facility_information, report_year)

    # Surcharge de la méthode format_output pour un format basique
    # Override of the format_output method for a basic format
    def format_output(self):
        """
        Format the record in basic style: year | facility_name | emissions units.

        Returns:
            str: Basic formatted string.
        """
        # Retourne une chaîne formatée basique avec année, nom de l'installation, et émissions
        # Returns a basic formatted string with year, facility name, and emissions
        return (f"{self.report_year} | {self.facility_name} | {self.emissions} {self.units}")