import json
import pathlib


class AuthSecret:
    """Auth manager for reddit api oauth"""
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"AuthSecret(username='{self.username}',password='*****')"

    @classmethod
    def from_json_config(cls, config_json_path:pathlib.Path):
        """Create instance from json config

        Args:
            config_json_path:   path to config file containing secrets
        """

        with open(config_json_path, 'r') as fin:
            data = json.load(fin)

        username = data['REDDIT_USERNAME']
        password = data['REDDIT_PASSWORD']
        return cls(username=username, password=password)
