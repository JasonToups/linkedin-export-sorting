# LinkedIn Messaging List of Profile URLs

If you would like to get a list of Profile URLs from your LinkedIn Messages, you can run this script to get a CSV file with a list of the URLs.

Then you can take that list of profile URLs and use something like [Phantombuster](https://phantombuster.com) to create a campaign where you can send automated messages to your list, which would include their name and company.

## Setting up this Project

### Get your LinkedIn Profile URL

Go to [LinkedIn](https://www.linkedin.com) and view your **Profile**.

_Copy_ the URL.

> This will remove your Profile URL from the sorted output list.

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
9. Click the link in the email to download a ZIP file containing your LinkedIn messages and any other data you selected to your Downloads folder.
10. The downloaded ZIP file will contain a CSV file with your LinkedIn messages, including the message content, sender, recipient, and timestamp information.

> Note that you can only export messages from connections who have allowed their email addresses to be visible to connections.

### Run the Script

Execute the bash script that:

1. Creates the virtual env.
2. Installs requirements.
3. Runs sorted-urlList.py
4. Deactivates the virtual env.

- The script will prompt you for your LinkedIn username.
- Recommended to use default (just hit Enter) for Source Path and Output Path. It will smartly search your Downloads folder for messages.csv and save linkedin_urls.csv to your Downloads folder.

```bash
./run.sh
```
