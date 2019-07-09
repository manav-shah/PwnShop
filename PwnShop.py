import requests
account='shahmanav789@gmail.com'
breachdata=requests.get(f'https://haveibeenpwned.com/api/v2/breachedaccount/{account}')

try:
    breachdata.raise_for_status()
except Exception as exc:
    print(f'The following error was encountered: {exc}')

tempfile=open('tempfile.txt','wb')
for chunk in breachdata.iter_content():
    tempfile.write(chunk)
tempfile.close()