import gspread
from pprint import pprint
from oauth2client.service_account import ServiceAccountCredentials
scope = ["https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)
client = gspread.authorize(creds)
sheet = client.open("new").sheet1
data = sheet.get_all_records()
x = len(data)+1
email = "myemail@gmail.com"
phone_no = "22222222222"
address = "nig sector c ed nagar ghunnao"

insertRow = [x,email,phone_no,address]

row = sheet.insert_row(insertRow,x+1)
pprint(row)