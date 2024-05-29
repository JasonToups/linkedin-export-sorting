import csv

# Set to store unique LinkedIn URLs
linkedin_urls = set()

# Open the CSV file
with open('messages-format-for-GoogleSheets.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        # Extract LinkedIn URLs from the 4th and 6th columns
        linkedin_urls.add(row[3])
        linkedin_urls.add(row[5])

# Remove empty strings
linkedin_urls.discard('')

# Write the unique LinkedIn URLs to a new CSV file
with open('linkedin_urls.csv', 'w') as f:
    writer = csv.writer(f)
    for url in linkedin_urls:
        writer.writerow([url])