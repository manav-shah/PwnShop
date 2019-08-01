import smtplib

def sendmail(email,message):
    port = 465
    with smtplib.SMTP_SSL(host='smtp.gmail.com',port=port) as SMTPObj:
        SMTPObj.ehlo()
        SMTPObj.login(user='ppwnshop@gmail.com',password='pwnshop_py')
        message = '''Subject: PwnShop results \n''' + message
        SMTPObj.sendmail('ppwnshop@gmail.com','manavoffer@gmail.com',message)


    