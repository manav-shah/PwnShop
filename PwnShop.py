import requests
import sys
import pandas as pd
from emailFunc import sendmail
#account='shahmanav789@gmail.com'
#account='somefakeemail_v2@gmail.com'

def pwncheck(account):
    url = f'https://haveibeenpwned.com/api/v2/breachedaccount/{account}'
    res=requests.get(url)

    #Catch any http errors
    try:
        res.raise_for_status()
        breachdata = res.json()
        num_of_breaches=len(breachdata)
        isbreached = True
        message = [f"""Uh-oh! Looks like you've been pwned. Your account was found in {num_of_breaches} breaches.\nThese are the detected breaches:\n"""]

    except requests.HTTPError as exception:

        isbreached = False
        if res.status_code == 404: #Not Found Error
            message = ["You haven't been pwned (yet)! There were no detected breaches for the given email address."]
        else:
            message = [f'Sorry, there was an error. The following error was encountered: {exception} \n']

    if isbreached:
        #Convert breachdata from list of dicts to dataframe, so it is easier to sort by added date.
        df = pd.DataFrame(breachdata).sort_values(by='AddedDate',ascending=False)
        domains = [i for i in df['Domain']]
        addeddate = [i for i in df['AddedDate']]
        for domain,date in zip(domains,addeddate):
            message.append(f'{domain} added  on {date}\n')
        message.append(f'For more details, go here: {url}')

    message = ''.join(message)
    return message


def main():
    account=sys.argv[0]
    message=pwncheck(account)
    sendmail(account,message)
    
if __name__ == '__main__':
    main()
