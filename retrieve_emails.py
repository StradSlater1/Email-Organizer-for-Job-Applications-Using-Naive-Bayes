from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import pandas as pd

creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/gmail.readonly'])

service = build('gmail', 'v1', credentials=creds)

start_date = '2023/08/21'
end_date = '2024/04/30'

# Use the 'q' parameter to filter emails between the specified dates
query = f'after:{start_date} before:{end_date}'
results = service.users().messages().list(userId='me', q=query).execute()
emails = []
page_token = None

# Retrieve all emails using pagination
while True:
    results = service.users().messages().list(userId='me', q=query, pageToken=page_token).execute()
    emails.extend(results.get('messages', []))
    page_token = results.get('nextPageToken')
    if not page_token:
        break

snippets = []

for email in emails:
    email_id = email['id']

    message = service.users().messages().get(userId='me', id=email_id).execute()
    snippet = message['snippet']
    snippets.append(snippet)
    print(snippet)
print(len(snippets))

data = {'email' : snippets}
df = pd.DataFrame(data)
df.to_csv('emails.csv')