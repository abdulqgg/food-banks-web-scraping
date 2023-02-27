import csv

# Open the text file for reading
with open('foodbank_data_1.txt', 'r') as f:
    # Read all lines in the file
    lines = f.readlines()

# Create an empty list to store the data
data = []
# Create an empty dictionary to store the current item
current_item = {}

# Loop through all lines in the file
for line in lines:
    # If the line is a separator (denoted by '##' or '##\n'), append the current item to the data list and start a new item
    if line == '##\n' or line == '##':
        data.append(current_item)
        current_item = {}
    else:
        # Otherwise, split the line into key and value and add it to the current item dictionary
        key, value = line.strip().split('§')
        current_item[key] = value

# Open the CSV file for writing
with open('data.csv', 'w', newline='') as f:
    # Create a CSV writer using DictWriter and write the header row
    writer = csv.DictWriter(f, fieldnames=['Organisation', 'Postcode', 'Website', 'Facebook', 'Twitter'])
    writer.writeheader()
    
    # Loop through all items in the data list and write each item as a row in the CSV file
    for item in data:
        writer.writerow(item)

