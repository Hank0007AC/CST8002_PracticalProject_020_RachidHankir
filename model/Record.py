"""
CST8002 Programming Language Research Project
Practical Project Part 03
Professor: Tyler DeLay
Due Date: 07/13/2025
Author: Rachid Hankir
"""

from abc import ABC, abstractmethod

# Classe abstraite super-classe pour représenter un enregistrement d'émission
# Abstract super-class to represent an emission record
class Record(ABC):
    """
    Abstract super-class for emission records, defining common attributes and polymorphic output method.
    """
    # Constructeur pour initialiser les attributs communs des enregistrements
    # Constructor to initialize common attributes of records
    def __init__(self, npri_id, facility_name, company_name, address, city, province, postal_code, latitude, longitude, emissions, units, facility_details, facility_information, report_year):
        """
        Initialize a Record with data from the dataset.

        Args:
            npri_id (str): The NPRI ID of the facility.
            facility_name (str): The name of the facility.
            company_name (str): The name of the company.
            address (str): The address of the facility.
            city (str): The city where the facility is located.
            province (str): The province where the facility is located.
            postal_code (str): The postal code of the facility.
            latitude (float): The latitude of the facility.
            longitude (float): The longitude of the facility.
            emissions (float): The emission value.
            units (str): The unit of measurement for emissions.
            facility_details (str): Additional details about the facility.
            facility_information (str): Additional information about the facility.
            report_year (int): The year of the report.
        """
        # Attribution des valeurs aux attributs privés pour encapsulation et héritage
        # Assignment of values to private attributes for encapsulation and inheritance
        self._npri_id = npri_id
        self._facility_name = facility_name
        self._company_name = company_name
        self._address = address
        self._city = city
        self._province = province
        self._postal_code = postal_code
        self._latitude = float(latitude) if latitude else 0.0
        self._longitude = float(longitude) if longitude else 0.0
        self._emissions = float(emissions) if emissions else 0.0
        self._units = units
        self._facility_details = facility_details
        self._facility_information = facility_information
        self._report_year = int(report_year) if report_year else 0

    # Méthode abstraite pour le format de sortie, à surcharger dans les sous-classes
    # Abstract method for output format, to be overridden in subclasses
    @abstractmethod
    def format_output(self):
        """
        Abstract method to format the record output (polymorphic).

        Returns:
            str: Formatted string representation of the record.
        """
        pass

    # Getters et Setters pour chaque attribut (communs à toutes les sous-classes)
    # Getters and Setters for each attribute (common to all subclasses)
    @property
    def npri_id(self):
        """Get the NPRI ID."""
        # Retourne l'ID NPRI stocké
        # Returns the stored NPRI ID
        return self._npri_id

    @npri_id.setter
    def npri_id(self, value):
        """Set the NPRI ID."""
        # Définit une nouvelle valeur pour l'ID NPRI
        # Sets a new value for the NPRI ID
        self._npri_id = value

    @property
    def facility_name(self):
        """Get the facility name."""
        # Retourne le nom de l'installation
        # Returns the facility name
        return self._facility_name

    @facility_name.setter
    def facility_name(self, value):
        """Set the facility name."""
        # Définit une nouvelle valeur pour le nom de l'installation
        # Sets a new value for the facility name
        self._facility_name = value

    @property
    def company_name(self):
        """Get the company name."""
        # Retourne le nom de l'entreprise
        # Returns the company name
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        """Set the company name."""
        # Définit une nouvelle valeur pour le nom de l'entreprise
        # Sets a new value for the company name
        self._company_name = value

    @property
    def address(self):
        """Get the address."""
        # Retourne l'adresse
        # Returns the address
        return self._address

    @address.setter
    def address(self, value):
        """Set the address."""
        # Définit une nouvelle valeur pour l'adresse
        # Sets a new value for the address
        self._address = value

    @property
    def city(self):
        """Get the city."""
        # Retourne la ville
        # Returns the city
        return self._city

    @city.setter
    def city(self, value):
        """Set the city."""
        # Définit une nouvelle valeur pour la ville
        # Sets a new value for the city
        self._city = value

    @property
    def province(self):
        """Get the province."""
        # Retourne la province
        # Returns the province
        return self._province

    @province.setter
    def province(self, value):
        """Set the province."""
        # Définit une nouvelle valeur pour la province
        # Sets a new value for the province
        self._province = value

    @property
    def postal_code(self):
        """Get the postal code."""
        # Retourne le code postal
        # Returns the postal code
        return self._postal_code

    @postal_code.setter
    def postal_code(self, value):
        """Set the postal code."""
        # Définit une nouvelle valeur pour le code postal
        # Sets a new value for the postal code
        self._postal_code = value

    @property
    def latitude(self):
        """Get the latitude."""
        # Retourne la latitude
        # Returns the latitude
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        """Set the latitude."""
        # Définit une nouvelle valeur pour la latitude, convertie en float
        # Sets a new value for the latitude, converted to float
        self._latitude = float(value) if value else 0.0

    @property
    def longitude(self):
        """Get the longitude."""
        # Retourne la longitude
        # Returns the longitude
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        """Set the longitude."""
        # Définit une nouvelle valeur pour la longitude, convertie en float
        # Sets a new value for the longitude, converted to float
        self._longitude = float(value) if value else 0.0

    @property
    def emissions(self):
        """Get the emissions value."""
        # Retourne la valeur des émissions
        # Returns the emissions value
        return self._emissions

    @emissions.setter
    def emissions(self, value):
        """Set the emissions value."""
        # Définit une nouvelle valeur pour les émissions, convertie en float
        # Sets a new value for the emissions, converted to float
        self._emissions = float(value) if value else 0.0

    @property
    def units(self):
        """Get the units of measurement."""
        # Retourne les unités de mesure
        # Returns the units of measurement
        return self._units

    @units.setter
    def units(self, value):
        """Set the units of measurement."""
        # Définit une nouvelle valeur pour les unités
        # Sets a new value for the units
        self._units = value

    @property
    def facility_details(self):
        """Get the facility details."""
        # Retourne les détails supplémentaires
        # Returns the additional details
        return self._facility_details

    @facility_details.setter
    def facility_details(self, value):
        """Set the facility details."""
        # Définit une nouvelle valeur pour les détails supplémentaires
        # Sets a new value for the additional details
        self._facility_details = value

    @property
    def facility_information(self):
        """Get the facility information."""
        # Retourne les informations supplémentaires
        # Returns the additional information
        return self._facility_information

    @facility_information.setter
    def facility_information(self, value):
        """Set the facility information."""
        # Définit une nouvelle valeur pour les informations supplémentaires
        # Sets a new value for the additional information
        self._facility_information = value

    @property
    def report_year(self):
        """Get the report year."""
        # Retourne l'année du rapport
        # Returns the report year
        return self._report_year

    @report_year.setter
    def report_year(self, value):
        """Set the report year."""
        # Définit une nouvelle valeur pour l'année, convertie en entier
        # Sets a new value for the report year, converted to integer
        self._report_year = int(value) if value else 0

    # Méthode __str__ pour utiliser format_output par défaut
    # __str__ method to use format_output by default
    def __str__(self):
        """
        Return a string representation using the polymorphic format_output method.

        Returns:
            str: Formatted string representation of the record.
        """
        # Appelle la méthode polymorphe format_output
        # Calls the polymorphic format_output method
        return self.format_output()