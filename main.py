import csv
from EmissionRecord import EmissionRecord

def read_emission_data(filename, max_records=5):
    records = []
    encodings = ['utf-8', 'latin-1']
    for encoding in encodings:
        try:
            with open(filename, mode='r', encoding=encoding) as file:
                csv_reader = csv.reader(file)
                next(csv_reader, None)
                for row, _ in zip(csv_reader, range(max_records)):
                    while len(row) < 14:
                        row.append('')
                    record = EmissionRecord(
                        npri_id=row[0],
                        facility_name=row[1],
                        company_name=row[2],
                        address=row[3],
                        city=row[4],
                        province=row[5],
                        postal_code=row[6],
                        latitude=row[7],
                        longitude=row[8],
                        emissions=row[9],
                        units=row[10],
                        facility_details=row[11],
                        facility_information=row[12],
                        report_year=row[13]
                    )
                    records.append(record)
                return records
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
            return []
        except UnicodeDecodeError:
            if encoding == encodings[-1]:
                print(f"Error: Unable to decode file '{filename}' with tried encodings.")
                return []
            continue
        except Exception as e:
            print(f"Error reading file with {encoding}: {e}")
            return []
    return []

def display_records(records):
    if not records:
        print("No records to display.")
        return
    print(f"Loaded {len(records)} records.\n")
    for record in records:
        print(record)

def main():
    filename = "Nitrogen oxide emissions by facility.csv"
    emission_records = read_emission_data(filename)
    
    print("Emission Records:")
    display_records(emission_records)

if __name__ == "__main__":
    main()