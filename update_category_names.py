import csv

def update_category_names(log_file_path, output_csv_path):
    categories = {}
    localID = None  # Initialize localID to None outside the loop

    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            line = line.strip()
            if line.startswith('*** Category ***'):
                localID = None  # Reset localID at the start of a new category
            elif line.startswith('localID:'):
                localID = str(line.split(':', 1)[1].strip())  # Update localID
            elif line.startswith('name:') and localID is not None:
                name = line.split(':', 1)[1].strip()
                categories[localID] = name  # Only add to categories if localID is set

    print(f"Loaded categories: {len(categories)} categories found.")  # Debugging output

    updated_rows = []
    with open(output_csv_path, mode='r', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            category_id = str(row['categoryLocal'])
            if category_id in categories:
                row['categoryLocal'] = categories[category_id]
            updated_rows.append(row)

    # Debugging output to check if replacements are happening
    if updated_rows:
        print("Sample updated row:", updated_rows[0])
    else:
        print("No rows to update")

    with open(output_csv_path, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(updated_rows)

    print("CSV file has been updated with category names.")

