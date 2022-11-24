from config_utils.api import Config
from email_parser import parse
from email_utils import imap_login, read_unread_emails
from excel_utils import append_to_excel_file

import schedule


def main(config):
    imap = imap_login(config)
    emails = read_unread_emails(imap, config.get_email_ids())
    records = parse(emails, config)
    append_to_excel_file(config, records)


if __name__ == '__main__':
    _config = Config('../config.json')
    schedule.every(5).minutes.do(main, _config)
