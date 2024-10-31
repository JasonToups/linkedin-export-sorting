import os
import re

def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'Downloads')

def find_messages_csv():
    """Finds messages.csv inside your Downloads folder"""
    # Define the regex pattern to match the folder name
    folder_pattern = re.compile(r'Basic_LinkedInDataExport_\d{2}-\d{2}-\d{4}', re.IGNORECASE)

    # Iterate through the directory
    for root, dirs, files in os.walk(get_download_path()):
        # Check if the current directory matches the pattern
        if folder_pattern.search(os.path.basename(root)):
            # Look for messages.csv in the current directory
            if 'messages.csv' in files:
                # Return the absolute path of messages.csv
                return os.path.join(root, 'messages.csv')
    
    return None  # Return None if not found
