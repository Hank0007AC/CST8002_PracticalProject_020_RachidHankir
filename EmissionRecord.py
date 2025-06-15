"""
CST8002 Programming Language Research Project
Practical Project Part 02
Professor: Stanley Pieda
Due Date: 06/15/2025
Author: Rachid Hankir
"""

# Importation de la classe EmissionRecord pour représenter chaque enregistrement du dataset
class EmissionRecord:
    """
    A class to represent a single record from the emissions dataset.
    Each attribute corresponds to a column in the dataset.
    """
    # Constructeur pour initialiser un objet EmissionRecord avec les données du dataset
    def __init__(self, npri_id, facility_name, company_name, address, city, province, postal_code, latitude, longitude, emissions, units, facility_details, facility_information, report_year):
        """
        Initialize an EmissionRecord with data from the dataset.

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
        # Attribution de l'ID NPRI à une variable privée pour encapsulation
        self._npri_id = npri_id
        # Stockage du nom de l'installation
        self._facility_name = facility_name
        # Stockage du nom de l'entreprise
        self._company_name = company_name
        # Stockage de l'adresse
        self._address = address
        # Stockage de la ville
        self._city = city
        # Stockage de la province
        self._province = province
        # Stockage du code postal
        self._postal_code = postal_code
        # Conversion de la latitude en float, avec 0.0 si vide pour éviter les erreurs
        self._latitude = float(latitude) if latitude else 0.0
        # Conversion de la longitude en float, avec 0.0 si vide
        self._longitude = float(longitude) if longitude else 0.0
        # Conversion des émissions en float, avec 0.0 si vide
        self._emissions = float(emissions) if emissions else 0.0
        # Stockage des unités de mesure
        self._units = units
        # Stockage des détails supplémentaires de l'installation
        self._facility_details = facility_details
        # Stockage des informations supplémentaires
        self._facility_information = facility_information
        # Conversion de l'année en entier, avec 0 si vide
        self._report_year = int(report_year) if report_year else 0

    # Getter pour l'ID NPRI
    @property
    def npri_id(self):
        """Get the NPRI ID."""
        # Retourne l'ID NPRI stocké
        return self._npri_id

    # Getter pour le nom de l'installation
    @property
    def facility_name(self):
        """Get the facility name."""
        # Retourne le nom de l'installation
        return self._facility_name

    # Getter pour le nom de l'entreprise
    @property
    def company_name(self):
        """Get the company name."""
        # Retourne le nom de l'entreprise
        return self._company_name

    # Getter pour l'adresse
    @property
    def address(self):
        """Get the address."""
        # Retourne l'adresse
        return self._address

    # Getter pour la ville
    @property
    def city(self):
        """Get the city."""
        # Retourne la ville
        return self._city

    # Getter pour la province
    @property
    def province(self):
        """Get the province."""
        # Retourne la province
        return self._province

    # Getter pour le code postal
    @property
    def postal_code(self):
        """Get the postal code."""
        # Retourne le code postal
        return self._postal_code

    # Getter pour la latitude
    @property
    def latitude(self):
        """Get the latitude."""
        # Retourne la latitude
        return self._latitude

    # Getter pour la longitude
    @property
    def longitude(self):
        """Get the longitude."""
        # Retourne la longitude
        return self._longitude

    # Getter pour les émissions
    @property
    def emissions(self):
        """Get the emissions value."""
        # Retourne la valeur des émissions
        return self._emissions

    # Getter pour les unités
    @property
    def units(self):
        """Get the units of measurement."""
        # Retourne les unités de mesure
        return self._units

    # Getter pour les détails de l'installation
    @property
    def facility_details(self):
        """Get the facility details."""
        # Retourne les détails supplémentaires
        return self._facility_details

    # Getter pour les informations supplémentaires
    @property
    def facility_information(self):
        """Get the facility information."""
        # Retourne les informations supplémentaires
        return self._facility_information

    # Getter pour l'année
    @property
    def report_year(self):
        """Get the report year."""
        # Retourne l'année du rapport
        return self._report_year

    # Méthode pour formater l'affichage de l'objet
    def __str__(self):
        """
        Return a string representation of the EmissionRecord.

        Returns:
            str: A formatted string containing key record attributes.
        """
        # Retourne une chaîne formatée avec l'année, le nom, la ville et les émissions
        return (f"{self._report_year} | {self._facility_name} | {self._city} | {self._emissions} {self._units}")