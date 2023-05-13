import csv

# Open the CSV file
with open('DigitalCurrencyList.csv', mode='r') as file:

    # Create a CSV reader using DictReader function
    csv_reader = csv.DictReader(file)

    # Create an empty dictionary to store the data
    data = {}

    # Loop through each row in the CSV file
    for row in csv_reader:

        # Get the value of the first column (assumed to be unique)
        key = row.pop('currency name')

        # Store the remaining columns in the dictionary with the key as the key
        data[key] = row['currency code']

# Print the dictionary
print(data)
