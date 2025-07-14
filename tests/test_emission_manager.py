"""
CST8002 Programming Language Research Project
Practical Project Part 03
Professor: Tyler DeLay
Due Date: 07/13/2025
Author: Rachid Hankir
"""

import pytest
from business.emission_manager import EmissionManager
from model.BasicEmissionRecord import BasicEmissionRecord
from model.DetailedEmissionRecord import DetailedEmissionRecord

# Test unitaire pour vérifier le polymorphisme des formats de sortie
# Unit test to verify polymorphism of output formats
def test_polymorphic_output():
    """
    Test polymorphic output formats for Basic and Detailed EmissionRecords in EmissionManager.
    """
    # Initialisation du gestionnaire
    # Initialize the manager
    manager = EmissionManager()

    # Créer un enregistrement basique
    # Create a basic record
    basic_record = manager.create_record(
        npri_id="999",
        facility_name="Test Facility",
        company_name="Test Company",
        address="123 Test St",
        city="Test City",
        province="ON",
        postal_code="K1A0B1",
        latitude=45.0,
        longitude=-75.0,
        emissions=100.0,
        units="Tonnes",
        facility_details="Test Details",
        facility_information="Test Info",
        report_year=2023,
        format_type='basic'
    )

    # Créer un enregistrement détaillé
    # Create a detailed record
    detailed_record = manager.create_record(
        npri_id="1000",
        facility_name="Test Facility 2",
        company_name="Test Company 2",
        address="456 Test Ave",
        city="Test City 2",
        province="QC",
        postal_code="G1A1B1",
        latitude=46.0,
        longitude=-71.0,
        emissions=200.0,
        units="Tonnes",
        facility_details="Test Details 2",
        facility_information="Test Info 2",
        report_year=2024,
        format_type='detailed'
    )

    # Vérifier que les enregistrements sont ajoutés
    # Verify that the records are added
    assert len(manager.get_records()) == 2

    # Vérifier le format basique
    # Verify the basic format
    assert basic_record.format_output() == "2023 | Test Facility | 100.0 Tonnes"

    # Vérifier le format détaillé
    # Verify the detailed format
    assert detailed_record.format_output() == "2024 | Test Facility 2 | Test Company 2 | Test City 2 | 200.0 Tonnes"

    # Afficher le nom pour la capture d'écran
    # Display the name for the screenshot
    print(f"Unit test completed. Prepared by Rachid Hankir")