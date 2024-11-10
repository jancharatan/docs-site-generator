import functools
import os.path

from collections import namedtuple

from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

from file_utils import extract_plaintext_from_google_doc

SCOPES = [
    'https://www.googleapis.com/auth/drive.metadata.readonly',
    'https://www.googleapis.com/auth/documents.readonly'
]

File = namedtuple('File', ['id', 'name'])

def get_credentials():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
    with open("token.json", "w") as token:
        token.write(creds.to_json())
    return creds

def api_exceptions(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except HttpError as e:
            print(f"A HttpError occurred: {e}")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    return wrapper

@api_exceptions
def get_folder_id(folder_name: str, service: build) -> str:
    items = (
        service.files()
        .list(pageSize=1, q=f"name = '{folder_name}' and trashed = false", fields="nextPageToken, files(id)")
        .execute()
    ).get("files", [])
    return items[0]['id'] if len(items) == 1 else None

@api_exceptions
def get_files_in_folder(folder_id: str, service: build) -> list[File]:
    results = service.files().list(q=f"'{folder_id}' in parents and trashed = false", fields="files(id, name)").execute()
    files = results.get('files', [])
    return [File(file.get('id'), file.get('name')) for file in files]

@api_exceptions
def get_content(file: File, docs_service: build):
    google_doc = docs_service.documents().get(documentId=file.id).execute()
    return extract_plaintext_from_google_doc(google_doc)
