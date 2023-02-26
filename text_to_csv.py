import csv

# Open the input text file
with open('foodbank_data_test.txt', 'r') as infile:
    # Read the lines into a list
    lines = infile.readlines()

# Create a list to hold the data
data = []

# Loop through the lines and extract the values
for line in lines:
    # Split the line into key-value pairs
    parts = line.strip().split(':')
    # Extract the key and value
    key = parts[0].strip()
    value = parts[1].strip()
    # Append the data to the list
    data.append((key, value))

# Open the output CSV file
with open('output.csv', 'w', newline='') as outfile:
    # Create a CSV writer object
    writer = csv.writer(outfile)
    # Write the header row
    writer.writerow(['Key', 'Value'])
    # Write the data rows
    for row in data:
        writer.writerow(row)
