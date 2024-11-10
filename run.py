from googleapiclient.discovery import build
from google_api_accessor import get_credentials, get_folder_id, get_files_in_folder

def main():
    folder_name = "docs-site-generator"
    service = build("drive", "v3", credentials=get_credentials())
    folder_id = get_folder_id(folder_name, service)
    files = get_files_in_folder(folder_id, service)

    print(files)    

if __name__ == "__main__":
  main()