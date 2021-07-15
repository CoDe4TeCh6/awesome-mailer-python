import smtplib
def send_my_Mail(my_mail, my_pass, mail_to, content):
    '''send mail to anybody without opening gmail'''
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(my_mail, my_pass)
    server.sendmail(my_mail, mail_to, content)
    server.close()
    print("Mail Transfered!")
send_my_Mail("yourmail@gmail.com","your_password","mail_reciever@gmail.com","your content")