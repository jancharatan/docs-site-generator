from googleapiclient.discovery import build
from google_api_accessor import get_credentials, get_folder_id, get_files_in_folder, get_content

def main():
    folder_name = "docs-site-generator"
    credentials = get_credentials()

    drive_service = build("drive", "v3", credentials=credentials)
    folder_id = get_folder_id(folder_name, drive_service)
    files = get_files_in_folder(folder_id, drive_service)

    docs_service = build('docs', 'v1', credentials=credentials)
    for file_id in files:
       print(get_content(file_id, docs_service))

if __name__ == "__main__":
  main()