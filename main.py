import csv

# Import the function from the update_category_names.py file
from update_category_names import update_category_names

log_file_path = 'input'
output_csv_path = 'output.csv'
batch_size = 100  # Editable batch size for processing

# Specify the fields of interest
fields_of_interest = ['amount', 'categoryLocal', 'date', 'note']

# Function to generate a unique identifier for an item
def create_unique_id(item):
    # Adjust the unique ID creation logic based on your needs
    return f"{item.get('date', '')}-{item.get('amount', '')}-{item.get('categoryLocal', '')}-{item.get('note', '')}"

print("Starting to read and process the log file...")
item_counter = 0
batch = []
unique_items = set()  # Set to store unique identifiers

# Start reading the log file and writing to the CSV file
with open(output_csv_path, 'w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fields_of_interest)
    csv_writer.writeheader()

    with open(log_file_path, 'r') as log_file:
        current_item = {}
        inside_item = False

        for line in log_file:
            line = line.strip()
            if line == '*** Item ***':
                if current_item:  # Check if there's a previous item
                    unique_id = create_unique_id(current_item)
                    if unique_id not in unique_items:  # Check for uniqueness
                        unique_items.add(unique_id)
                        batch.append(current_item)
                        item_counter += 1
                        if len(batch) >= batch_size:
                            csv_writer.writerows(batch)
                            batch.clear()
                            print(f"Processed and written {item_counter} items...")
                current_item = {}
                inside_item = True
                continue

            if inside_item and ': ' in line:
                key, value = line.split(': ', 1)
                if key.strip() in fields_of_interest:
                    current_item[key.strip()] = value.strip()

        # Handle the last item
        if current_item:
            unique_id = create_unique_id(current_item)
            if unique_id not in unique_items:
                batch.append(current_item)
                item_counter += 1
        
        # Write any remaining items in the batch
        if batch:
            csv_writer.writerows(batch)
            print(f"Finalizing. Processed and written all {item_counter} items...")

print(f"CSV file generation complete. Total unique items processed and written: {item_counter}")


# Start the category name update process (Not working!)
# print("Starting to update category names...")
# update_category_names(log_file_path, output_csv_path)

# print(f"All done. Check the \"{output_csv_path}\" file for the updated data.")
