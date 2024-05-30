# LinkedIn Messaging List of Profile URLs

If you would like to get a list of Profile URLs from your LinkedIn Messages, you can run this script to get a CSV file with a list of the URLs.

Then you can take that list of profile URLs and use something like [Phantombuster](https://phantombuster.com) to create a campaign where you can send automated messages to your list, which would include their name and company.

## Setting up this Project

### Export your Messages Data from LinkedIn

To export your messages data from LinkedIn, follow these steps:

1. Click the "Me" icon at the top of your LinkedIn homepage.
2. Select "Settings & Privacy" from the dropdown menu.
3. Click on "Data privacy" in the left sidebar.
4. Under "How LinkedIn uses your data", click "Get a copy of your data".
   Select "Want something in particular? Select the data files you're most interested in."
5. Check the box next to "Messages" to include your message history in the export.
6. Click "Request archive".
7. Enter your LinkedIn password when prompted and click "Done".
8. LinkedIn will then process your request. You'll receive an email notification with a link to download your data archive within 24 hours.
9. Click the link in the email to download a ZIP file containing your LinkedIn messages and any other data you selected.
10. The downloaded ZIP file will contain a CSV file with your LinkedIn messages, including the message content, sender, recipient, and timestamp information.

> Note that you can only export messages from connections who have allowed their email addresses to be visible to connections.

### Move your messages.csv

You will receive an email when your messages.csv is ready to download.

Download the file and place it in this project.

### Install Pandas & Dependencies

You will need to install several packages, and have `Python3` and `PIP` installed.

### Use a Virtual Environment to Run the Project

Creating a **virtual environment** _isolates your package installations from the system Python environment_, which will help avoid system-wide issues.

#### Create a Virtual Environment:

```shell
python3 -m venv hire-me
```

#### Activate the Virtual Environment:

```shell
source hire-me/bin/activate
```

#### Upgrade pip and Install Packages:

```shell
pip install --upgrade pip
```

#### Install Pandas in your Virtual Environment

```shell
python3 -m pip install pandas
```

### Execute the sorted-urlList.py Script

Now that you have your Virtual Environment setup, you can execute the Python Script to get your date-sorted URL list from your messages, starting with your latest message.

```shell
python3 sorted-urlList.py
```

Now you should see the sorted list of urls in the file `linkedin_urls.csv`

### Stop your Virtual Environment

When you have what you need, stop your Virtual Environment

```shell
deactivate
```

## How to Run after Initial Setup

If you would like to run this project again, then put your updated messages list in the root directory.

**Create a Virtual Environment:**

```shell
python3 -m venv hire-me
```

**Execute the sorted-urlList.py Script**

```shell
python3 sorted-urlList.py
```
