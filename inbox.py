import imaplib
import email

def read_inbox(user, password):
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(user, password)

    mail.select("inbox")
    result, data = mail.search(None, "ALL")

    mail_ids = data[0].split()

    for i in reversed(mail_ids[-5:]):
        result, msg_data = mail.fetch(i, "(RFC822)")

        raw_email = msg_data[0][1]
        msg = email.message_from_bytes(raw_email)

        print("From:", msg["from"])
        print("Subject:", msg["subject"])
        print("-" * 40)
