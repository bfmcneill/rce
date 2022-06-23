import json
import pathlib

class AppSecret:
    """Secret manager for reddit api"""
    def __init__(self, client_id, secret):
        self.client_id = client_id
        self.secret = secret


    def __repr__(self):
        return f"AppSecret(client_id='{self.client_id}',secret='*****')"

    @classmethod
    def from_json_config(cls, config_json_path: pathlib.Path):
        """Create instance from json config

        Args:
            config_json_path:   path to config file containing secrets
        """

        with open(config_json_path, 'r') as fin:
            data = json.load(fin)

        secret = data['REDDIT_SECRET']
        client_id = data['REDDIT_CLIENT_ID']
        return cls(client_id=client_id, secret=secret)
