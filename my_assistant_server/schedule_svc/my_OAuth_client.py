import pickle
import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os

module_dir = os.path.dirname(__file__)

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def make_credentials(user_id):
    creds = None

    # if there are already credentials, then use it
    if os.path.exists(module_dir + '/'+user_id+'_token.pickle'):
        with open(module_dir + '/'+user_id+'_token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # if there are no (valid) credentials availabel, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                    module_dir + '/client_secret.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credential for the next run
        with open(module_dir + '/'+user_id+'_token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds
