import email


def read_unread_emails(imap, from_emails=None):
    imap.select('INBOX')
    status, data = imap.search(None, '(UNSEEN)')
    unread_msg_nums = data[0].split()
    emails = []
    for e_id in unread_msg_nums:
        _, data = imap.fetch(e_id, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_bytes(raw_email)
        if from_emails is None or email_message['From'].split("<")[-1][:-1] in from_emails:
            emails.append({
                "from": email_message['From'].split("<")[-1][:-1],
                "email": email_message
            })
    return emails
