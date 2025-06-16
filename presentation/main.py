"""
CST8002 Programming Language Research Project
Professor: Stanley Pieda
Due Date: 06/15/2025
Author: Rachid Hankir
"""

import os
import sys
# Ajouter le dossier racine au chemin Python pour résoudre les importations
# Add the root directory to the Python path to resolve imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from business.emission_manager import EmissionManager

# Fonction pour afficher le menu interactif
# Function to display the interactive menu
def display_menu(full_name):
    """
    Display the interactive menu with the author's name.

    Args:
        full_name (str): The full name of the author.
    """
    # Afficher le menu avec le nom
    # Display the menu with the name
    print(f"\nProgram by {full_name}\n")
    print("1. Reload data from CSV")
    print("2. Save data to new CSV")
    print("3. Display all records")
    print("4. Display a specific record")
    print("5. Create a new record")
    print("6. Edit a record")
    print("7. Delete a record")
    print("8. Exit")
    print(f"\nPrepared by {full_name}\n")

# Fonction principale du programme
# Main function of the program
def main():
    """
    Main function to run the interactive emission record management program.
    """
    # Définition du nom complet
    # Define the full name
    full_name = "Rachid Hankir"
    # Initialisation du gestionnaire d'émissions
    # Initialize the emission manager
    manager = EmissionManager()
    # Nom du fichier CSV
    # CSV file name
    filename = "Nitrogen oxide emissions by facility.csv"
    # Charger les données initiales
    # Load initial data
    manager.reload_data(filename)

    while True:
        # Afficher le menu
        # Display the menu
        display_menu(full_name)
        # Obtenir le choix de l'utilisateur
        # Get the user's choice
        choice = input("Enter your choice (1-8): ")
        
        if choice == "1":
            # Recharger les données
            # Reload data
            if manager.reload_data(filename):
                print("Data reloaded successfully.")
            else:
                print("Failed to reload data.")
            # Capture d'écran : Rechargement des données
            # Screenshot: Data reloading
            input("Press Enter to continue...")

        elif choice == "2":
            # Sauvegarder les données
            # Save data
            output_file = manager.save_data()
            if output_file:
                print(f"Data saved to {output_file}")
            else:
                print("Failed to save data.")
            # Capture d'écran : Sauvegarde des données
            # Screenshot: Data saving
            input("Press Enter to continue...")

        elif choice == "3":
            # Afficher tous les enregistrements
            # Display all records
            manager.display_records()
            # Capture d'écran : Affichage de tous les enregistrements
            # Screenshot: Display all records
            input("Press Enter to continue...")

        elif choice == "4":
            # Afficher un enregistrement spécifique
            # Display a specific record
            try:
                index = int(input("Enter record index (1-based): ")) - 1
                manager.display_records(index)
            except (ValueError, IndexError):
                print("Invalid index.")
            # Capture d'écran : Affichage d’un enregistrement spécifique
            # Screenshot: Display specific record
            input("Press Enter to continue...")

        elif choice == "5":
            # Créer un nouvel enregistrement
            # Create a new record
            try:
                record = manager.create_record(
                    input("NPRI ID: "), input("Facility name: "), input("Company name: "),
                    input("Address: "), input("City: "), input("Province: "),
                    input("Postal code: "), input("Latitude: "), input("Longitude: "),
                    input("Emissions: "), input("Units: "), input("Facility details: "),
                    input("Facility information: "), input("Report year: ")
                )
                print(f"Record created: {record}")
            except ValueError as e:
                print(f"Invalid input: {e}")
            # Capture d'écran : Création d’un enregistrement
            # Screenshot: Record creation
            input("Press Enter to continue...")

        elif choice == "6":
            # Modifier un enregistrement
            # Edit a record
            try:
                index = int(input("Enter record index (1-based): ")) - 1
                print("Enter new values (leave blank to keep current):")
                if manager.edit_record(
                    index,
                    npri_id=input("NPRI ID: ") or None,
                    facility_name=input("Facility name: ") or None,
                    company_name=input("Company name: ") or None,
                    address=input("Address: ") or None,
                    city=input("City: ") or None,
                    province=input("Province: ") or None,
                    postal_code=input("Postal code: ") or None,
                    latitude=input("Latitude: ") or None,
                    longitude=input("Longitude: ") or None,
                    emissions=input("Emissions: ") or None,
                    units=input("Units: ") or None,
                    facility_details=input("Facility details: ") or None,
                    facility_information=input("Facility information: ") or None,
                    report_year=input("Report year: ") or None
                ):
                    print("Record updated successfully.")
                else:
                    print("Invalid index.")
            except ValueError as e:
                print(f"Invalid input: {e}")
            # Capture d'écran : Modification d’un enregistrement
            # Screenshot: Record editing
            input("Press Enter to continue...")

        elif choice == "7":
            # Supprimer un enregistrement
            # Delete a record
            try:
                index = int(input("Enter record index (1-based): ")) - 1
                if manager.delete_record(index):
                    print("Record deleted successfully.")
                else:
                    print("Invalid index.")
            except ValueError:
                print("Invalid index.")
            # Capture d'écran : Suppression d’un enregistrement
            # Screenshot: Record deletion
            input("Press Enter to continue...")

        elif choice == "8":
            # Quitter le programme
            # Exit the program
            print(f"Exiting program. Prepared by {full_name}")
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

# Exécution du programme si le fichier est lancé directement
# Run the program if the file is executed directly
if __name__ == "__main__":
    main()