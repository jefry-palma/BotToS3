from os import access
import dropbox
from dropbox.files import FileMetadata

def download(access_token,path,download_path):
    with dropbox.Dropbox(oauth2_access_token=access_token) as dbx:
        dbx.files_download_to_file(download_path=download_path,path=path)

def list_files(access_token):
    file_paths = []
    with dropbox.Dropbox(oauth2_access_token=access_token) as dbx:
        resp = dbx.files_list_folder(path='', recursive=True)
        for entry in resp.entries:
            if isinstance(entry,FileMetadata):
                file_paths.append(entry.path_lower)

    return file_paths