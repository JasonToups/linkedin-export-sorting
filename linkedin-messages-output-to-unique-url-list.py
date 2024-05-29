import csv
from urllib.parse import urlparse

# Set to store unique LinkedIn URLs
linkedin_urls = set()

# URL to exclude
url_to_exclude = 'https://www.linkedin.com/in/jasontoups'

# Open the CSV file
with open('messages.csv', 'r') as f:
  reader = csv.reader(f)
  for row in reader:
    # Extract LinkedIn URLs from the 4th and 6th columns
    urls = row[3].split(',') + row[5].split(',')
    for url in urls:
      # Remove any leading/trailing whitespaces
      url = url.strip()
      # Exclude empty strings and URLs to exclude
      if url != '' and url != url_to_exclude:
        # Parse the URL and check if it's valid
        parsed = urlparse(url)
        if parsed.scheme and parsed.netloc:
          linkedin_urls.add(url)

# Write the unique LinkedIn URLs to a new CSV file
with open('linkedin_urls.csv', 'w') as f:
  writer = csv.writer(f)
  for url in linkedin_urls:
    writer.writerow([url])