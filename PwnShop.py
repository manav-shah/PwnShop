import requests
account='shahmanav789@gmail.com'
#account='somefakeemail_v2@gmail.com'
res=requests.get(f'https://haveibeenpwned.com/api/v2/breachedaccount/{account}')

#Catch any http errors without stopping script
try:
    res.raise_for_status()
    breachdata = res.json()
    num_of_breaches=len(breachdata)
    isbreached = True
except requests.HTTPError as exception:
    if res.status_code == 404:
        message = "You haven't been pwned! There were no detected breaches for the given email address."
        isbreached = False
    print(f'The following error was encountered: {exception} \n')

#store breach data in a file for future lookup
#with open('tempfile.txt','wb') as tempfile:
#    tempfile.write(res.content)
    











