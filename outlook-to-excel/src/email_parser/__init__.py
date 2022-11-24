from email_parser.brocker import brocker_parser
from email_parser.newhome import newhome_parser

import importlib


def parse(emails, config):
    records = []
    for email in emails:
        parser_func = config.get_parser_func(email['from'])
        parser = getattr(importlib.import_module('email_parser'), parser_func)
        records.append(parser(email['email']))
    return records
