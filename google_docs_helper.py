import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/documents']
TOKEN_PATH = os.path.expanduser('~/.credentials/google-docs-token.json')
CREDENTIALS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'credentials.json')

def get_docs_service():
    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        os.makedirs(os.path.dirname(TOKEN_PATH), exist_ok=True)
        with open(TOKEN_PATH, 'w') as token:
            token.write(creds.to_json())
    service = build('docs', 'v1', credentials=creds)
    return service

def create_doc_with_text(title, text):
    service = get_docs_service()
    try:
        doc = service.documents().create(body={'title': title}).execute()
        doc_id = doc.get('documentId')
        requests = [
            {
                'insertText': {
                    'location': {'index': 1},
                    'text': text
                }
            }
        ]
        service.documents().batchUpdate(documentId=doc_id, body={'requests': requests}).execute()
        doc_url = f'https://docs.google.com/document/d/{doc_id}/edit'
        return doc_url
    except HttpError as error:
        print(f'An error occurred: {error}')
        return None 