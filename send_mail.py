import smtplib

def send_email(sender, password, receiver, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
        print("Mail Sent Successfully")
    except Exception as e:
        print("Error:", e)
    finally:
        server.quit()
