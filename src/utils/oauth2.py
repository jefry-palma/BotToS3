from dropbox import DropboxOAuth2FlowNoRedirect
import webbrowser
from utils.config import Config

'''
This example walks through a basic oauth flow using the existing long-lived token type
Populate your app key and app secret in order to run this locally
'''

def get_access_token():


    auth_flow = DropboxOAuth2FlowNoRedirect(Config.config['APP_KEY'], Config.config['APP_SECRET'])

    authorize_url = auth_flow.start()
    webbrowser.open(authorize_url)
    auth_code = input("Enter the authorization code here: ").strip()

    try:
        oauth_result = auth_flow.finish(auth_code)
        return oauth_result.access_token
    except Exception as e:
        return None
