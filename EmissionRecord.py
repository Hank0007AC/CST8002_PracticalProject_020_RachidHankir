"""
CST8002 Programming Language Research Project
Professor: Stanley Pieda
Due Date: 05/25/2025
Author: Rachid Hankir
"""

class EmissionRecord:
    """
    A class to represent a single record from the emissions dataset.
    Each attribute corresponds to a column in the dataset.
    """
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

    @property
    def npri_id(self):
        """Get the NPRI ID."""
        return self._npri_id

    @property
    def facility_name(self):
        """Get the facility name."""
        return self._facility_name

    @property
    def company_name(self):
        """Get the company name."""
        return self._company_name

    @property
    def address(self):
        """Get the address."""
        return self._address

    @property
    def city(self):
        """Get the city."""
        return self._city

    @property
    def province(self):
        """Get the province."""
        return self._province

    @property
    def postal_code(self):
        """Get the postal code."""
        return self._postal_code

    @property
    def latitude(self):
        """Get the latitude."""
        return self._latitude

    @property
    def longitude(self):
        """Get the longitude."""
        return self._longitude

    @property
    def emissions(self):
        """Get the emissions value."""
        return self._emissions

    @property
    def units(self):
        """Get the units of measurement."""
        return self._units

    @property
    def facility_details(self):
        """Get the facility details."""
        return self._facility_details

    @property
    def facility_information(self):
        """Get the facility information."""
        return self._facility_information

    @property
    def report_year(self):
        """Get the report year."""
        return self._report_year

    def __str__(self):
        """
        Return a string representation of the EmissionRecord.

        Returns:
            str: A formatted string containing key record attributes.
        """
        return (f"{self._report_year} | {self._facility_name} | {self._city} | {self._emissions} {self._units}")