from dropbox import files
import os
from utils.oauth2 import get_access_token
from box.box import download,list_files
from aws.aws import upload_to_s3
def run():
    access_token = get_access_token()
    file_list = list_files(access_token)
    for path in file_list:
        download(access_token,path,'temp')
        if path[0] == '/':
            path = path[1:]
        path = str(path).replace(' ','-')
        upload_to_s3('temp',path)
        os.remove('temp')

if __name__ == "__main__":
    run()