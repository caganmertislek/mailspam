import smtplib

smtpturu = str(input('SMTP:'))
server = smtplib.SMTP(smtpturu, 587)
server.starttls()
email = str(input('E-Posta Adresiniz:'))
password = str(input('Şifreniz:'))
server.login(email, password)
kime = str(input('Alıcı:'))
konu = str(input('Konu:'))
metin = str(input('Metin:'))
msg = f'Subject: {konu}\n\n{metin}'
spamno = int(0)
while True:
    server.sendmail(
        email,
        kime,
        msg
        )
    spamno = spamno + 1
    print(spamno, '. Spam Gönderildi!')
