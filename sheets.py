import os
import json
import gspread
from google.oauth2.service_account import Credentials

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


def get_sheet(sheet_id: str, tab_name: str = 'Market'):
    if os.getenv('GOOGLE_CREDENTIALS'):
        info = json.loads(os.getenv('GOOGLE_CREDENTIALS'))
        creds = Credentials.from_service_account_info(info, scopes=SCOPES)
    else:
        creds = Credentials.from_service_account_file('credentials.json', scopes=SCOPES)

    client = gspread.authorize(creds)
    sheet = client.open_by_key(sheet_id)
    try:
        return sheet.worksheet(tab_name)
    except gspread.WorksheetNotFound:
        return sheet.add_worksheet(title=tab_name, rows=1000, cols=20)
