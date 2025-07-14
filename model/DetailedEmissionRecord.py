"""
CST8002 Programming Language Research Project
Practical Project Part 03
Professor: Stanley Pieda
Due Date: 07/08/2025
Author: Rachid Hankir
"""

from model.Record import Record

# Sous-classe pour un format de sortie détaillé des enregistrements
# Sub-class for a detailed output format of records
class DetailedEmissionRecord(Record):
    """
    Sub-class of Record for detailed formatted emission records.
    """
    # Constructeur pour initialiser un DetailedEmissionRecord, appelant le super
    # Constructor to initialize a DetailedEmissionRecord, calling the super
    def __init__(self, npri_id, facility_name, company_name, address, city, province, postal_code, latitude, longitude, emissions, units, facility_details, facility_information, report_year):
        """
        Initialize a DetailedEmissionRecord with data from the dataset.

        Args:
            (Inherited from Record)
        """
        # Appel au constructeur de la super-classe Record
        # Call to the super-class Record constructor
        super().__init__(npri_id, facility_name, company_name, address, city, province, postal_code, latitude, longitude, emissions, units, facility_details, facility_information, report_year)

    # Surcharge de la méthode format_output pour un format détaillé
    # Override of the format_output method for a detailed format
    def format_output(self):
        """
        Format the record in detailed style: year | facility_name | company_name | city | emissions units.

        Returns:
            str: Detailed formatted string.
        """
        # Retourne une chaîne formatée détaillée avec année, nom de l'installation, nom de l'entreprise, ville, et émissions
        # Returns a detailed formatted string with year, facility name, company name, city, and emissions
        return (f"{self.report_year} | {self.facility_name} | {self.company_name} | {self.city} | {self.emissions} {self.units}")