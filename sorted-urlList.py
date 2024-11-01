import pandas as pd
import os
import argparse
from pathlib import Path
from utils import get_download_path, find_messages_csv


def parse_args():
    parser = argparse.ArgumentParser("Process args for LinkedIn Message Exporting")

    required = parser.add_argument_group('required arguments')
    required.add_argument(
        "-u", "--username", 
        help="Your LinkedIn profile username, found in the URL bar. Example: linkedin.com/in/<linkedin_username>",
        type=str,
        required=True
    )

    
    optional = parser.add_argument_group('optional arguments')    
    optional.add_argument(
        "-s", "--source",
        help="Path to your exported LinkedIn messages (messages.csv).",
        type=str,
        default=find_messages_csv()
    )
    optional.add_argument(
        "-o", "--output",
        help="relative path location where you want sorted LinkedIn urls to be sent.",
        type=str,
        default=f"{get_download_path()}/linkedin_urls.csv"    
    )
    return parser.parse_args()

if __name__== "__main__":
    args = parse_args()
    print(f"u: {args.username}, s: {args.source}, o: {args.output}")
    profile_url = f'https://www.linkedin.com/in/{args.username}'

    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(args.source)

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
    df_output.to_csv(args.output, index=False, header=False)

    print(f"Done! Saved urls to: {args.output}")