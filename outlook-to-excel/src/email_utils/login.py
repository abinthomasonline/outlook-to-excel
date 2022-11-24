import imaplib


def imap_login(config):
    imap = imaplib.IMAP4_SSL(config.imap_server)
    imap.login(config.username, config.password)
    return imap
