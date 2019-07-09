import requests,json
#account='shahmanav789@gmail.com'
account='whatismyname@gmail.com'
res=requests.get(f'https://haveibeenpwned.com/api/v2/breachedaccount/{account}')

#Catch any http errors without stopping script
try:
    res.raise_for_status()
except Exception as exc:
    print(f'The following error was encountered: {exc}')

#store breach data in a file for future lookup
with open('tempfile.txt','wb') as tempfile:
    tempfile.write(res.content)
    
breachdata = res.json()
num_of_breaches=len(breachdata)










