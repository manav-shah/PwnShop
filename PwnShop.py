import requests
import pandas as pd
#account='shahmanav789@gmail.com'
#account='somefakeemail_v2@gmail.com'
account = 'randomname@gmail.com'
res=requests.get(f'https://haveibeenpwned.com/api/v2/breachedaccount/{account}')

#Catch any http errors without stopping script
try:
    res.raise_for_status()
    breachdata = res.json()
    num_of_breaches=len(breachdata)
    isbreached = True
    message = f"""Uh-oh! Looks like you've been pwned. Your account was found in {num_of_breaches} breaches.\nThese are the detected breaches:\n"""
    
except requests.HTTPError as exception:
    isbreached = False
    if res.status_code == 404:
        message = "You haven't been pwned (yet)! There were no detected breaches for the given email address."
    else: 
        message = f'Sorry, there was an error. The following error was encountered: {exception} \n'

if isbreached:
    df = pd.DataFrame(breachdata).sort_values(by='AddedDate',ascending=False)
    domains = [i for i in df['Domain']]
    addeddate = [i for i in df['AddedDate']]
    for domain,date in zip(domains,addeddate):
        message += f'{domain} added to hipb on {date}\n'


print(message)
    #store breach data in a file for future lookup
#with open('tempfile.txt','wb') as tempfile:
#    tempfile.write(res.content)
    











