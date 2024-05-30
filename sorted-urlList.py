import pandas as pd

source = 'messages.csv'
output = 'linkedin_urls.csv'
profile_url = 'https://www.linkedin.com/in/jasontoups'

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(source)

# Convert the 'DATE' column to datetime format
df['DATE'] = pd.to_datetime(df['DATE'])

# Sort the DataFrame by the 'DATE' column
df_sorted = df.sort_values(by='DATE', ascending=False)

# Select only the 'SENDER PROFILE URL' columns
df_urls = df_sorted[['SENDER PROFILE URL']]

# Drop any duplicate URLs
df_dupes = df_urls.drop_duplicates()

# Remove the profile URL from the list
df_output = df_dupes[df_dupes['SENDER PROFILE URL'] != profile_url]

# Save the sorted URLs to a new CSV file
df_output.to_csv(output, index=False, header=False)
