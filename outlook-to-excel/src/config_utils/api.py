import json


class Config:
    def __init__(self, config_json_path):
        with open(config_json_path) as f:
            config = json.load(f)
        self.imap_server = config['imap_server']
        self.username = config['username']
        self.password = config['password']
        self.from_emails = {}
        self.load_from_emails(config['from_emails'])

    def load_from_emails(self, from_emails):
        for email in from_emails:
            self.from_emails[email['email']] = email['parser_func']

    def get_email_ids(self):
        return self.from_emails.keys()

    def get_parser_func(self, email_id):
        return self.from_emails[email_id]
