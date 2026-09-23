
import gspread
from google.oauth2.service_account import Credentials

scopes = ['https://www.googleapis.com/auth/spreadsheets']
creds = Credentials.from_service_account_file('credentials.json', scopes=scopes)
client = gspread.authorize(creds)

sheet = client.open_by_key('1-HPUT-dNmxCB5f8cMXVoT4ohNSPa8nlPyf-7S0k5uos')
ws = sheet.sheet1
ws.update([['hello', 'world']])
print('Write OK')