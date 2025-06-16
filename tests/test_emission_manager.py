"""
CST8002 Programming Language Research Project
Practical Project Part 02
Professor: Stanley Pieda
Due Date: 06/15/2025
Author: Rachid Hankir
"""

import pytest
from business.emission_manager import EmissionManager

# Test unitaire pour vérifier la création d'un nouvel enregistrement
# Unit test to verify the creation of a new record
def test_create_record():
    """
    Test the creation of a new emission record in EmissionManager.
    """
    # Initialisation du gestionnaire
    # Initialize the manager
    manager = EmissionManager()
    # Créer un nouvel enregistrement avec des données de test
    # Create a new record with test data
    record = manager.create_record(
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
        report_year=2023
    )
    # Vérifier que l'enregistrement a été ajouté
    # Verify that the record was added
    assert len(manager.get_records()) == 1
    # Vérifier les valeurs de l'enregistrement
    # Verify the record's values
    assert record.npri_id == "999"
    assert record.facility_name == "Test Facility"
    assert record.report_year == 2023
    # Afficher le nom pour la capture d'écran
    # Display the name for the screenshot
    print(f"Unit test completed. Prepared by Rachid Hankir")