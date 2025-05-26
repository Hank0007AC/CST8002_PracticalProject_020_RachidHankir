class EmissionRecord:
    def __init__(self, npri_id, facility_name, company_name, address, city, province, postal_code, latitude, longitude, emissions, units, facility_details, facility_information, report_year):
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
        return self._npri_id

    @property
    def facility_name(self):
        return self._facility_name

    @property
    def company_name(self):
        return self._company_name

    @property
    def address(self):
        return self._address

    @property
    def city(self):
        return self._city

    @property
    def province(self):
        return self._province

    @property
    def postal_code(self):
        return self._postal_code

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    @property
    def emissions(self):
        return self._emissions

    @property
    def units(self):
        return self._units

    @property
    def facility_details(self):
        return self._facility_details

    @property
    def facility_information(self):
        return self._facility_information

    @property
    def report_year(self):
        return self._report_year

    def __str__(self):
        return (f"{self._report_year} | {self._facility_name} | {self._city} | {self._emissions} {self._units}")