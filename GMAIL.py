import maillib

user=raw_input("Enter User Mail Address : ")
passwd=raw_input("Enter Password : ")
server=raw_input("Enter Mail Server (eg:smtp.gmail.com) : ")
port=raw_input("Enter Mail Server Port (587): ")

to_address=raw_input("Enter Receiver Address : ")
cc_address=raw_input("Enter CC Address : ")
subject=raw_input("Enter Mail Subject : ")
body=raw_input("Type Message Body and Hit Enter\n>")
attach=raw_input("Enter Attachment File Path : ")
mail=maillib.mail(user,passwd,server,port)
if attach=='':
    mail.sendMail(to_address,cc_address,subject,body)
else:
    mail.sendMail_attachment(to_address,cc_address,subject,body,attach)

