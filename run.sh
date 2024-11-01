#!/bin/bash

### SETUP ENVIRONMENT ###
export VENV_NAME="hire-me"

# Create virtual environment if it doesn't exist
if [ ! -d "$VENV_NAME" ]; then
    python3 -m venv "$VENV_NAME"
    echo "Created virtual environment '$VENV_NAME'"
else
    echo "Virtual environment '$VENV_NAME' already exists."
fi

# Activate virtual env
# Creating a **virtual environment** _isolates your package installations from the system Python environment_, which will help avoid system-wide issues.
source "$VENV_NAME"/bin/activate
echo "Activated virtual env."

# Upgrade pip
pip install --upgrade pip
echo "Upgraded pip."

# Install requirements
python3 -m pip install -r requirements.txt
echo "Installed requirements."

echo "Setup complete!" 


### RUN SCRIPT ###

# Prompt for LinkedIn username
read -p "Enter your LinkedIn username: " LINKEDIN_USERNAME
# Check if LinkedIn username is provided
if [ -z "$LINKEDIN_USERNAME" ]; then
    echo "Error: LinkedIn username is required. View on your LinkedIn profile url bar."
    deactivate
    exit 1
fi

# Prompt for optional source and output paths
read -p "Enter the source path (RECOMMENDED: leave blank for default, downloads folder): " SOURCE_PATH
read -p "Enter the output path (RECOMMENDED: leave blank for default, downloads folder): " OUTPUT_PATH

if [[ -n ${SOURCE_PATH} ]]; then 
    SOURCE_FLAG="-s '${SOURCE_PATH}'"
fi

if [[ -n ${OUTPUT_PATH} ]]; then 
    OUTPUT_FLAG="-o '${OUTPUT_PATH}'"
fi


# Run the Python script with args
python3 sorted-urlList.py -u "$LINKEDIN_USERNAME" ${SOURCE_FLAG} ${OUTPUT_FLAG}

# Deactivate the virtual environment
deactivate

echo "Done!"
